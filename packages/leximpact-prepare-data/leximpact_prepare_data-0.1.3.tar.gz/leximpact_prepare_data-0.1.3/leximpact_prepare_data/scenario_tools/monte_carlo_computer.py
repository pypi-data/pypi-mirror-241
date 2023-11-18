import json
import random
import unittest
from time import time

import pandas as pd
from numpy.random import choice
import numpy as np
from leximpact_common_python_libraries.config import Configuration
from sklearn.metrics import mean_absolute_percentage_error
from tqdm import tqdm

tc = unittest.TestCase()
config = Configuration(project_folder="leximpact-prepare-data")


def monte_carlo_simulation(bucket, debug=False):
    """
    Implementation d'une fonction probabilistique qui associe une valeur estimée pour une variable VAR
    dans l'ERFS-FPR selon
    la valeur d'une variable de référence VAR_REF, en utilisant des copules calculés à partir des
    distributions de VAR1 et VAR_REF dans POTE.
    Par exemple, VAR1 = Rk et VAR_REF = RFR

    ::bucket:: Dictionnaire contenant les caractéristiques du bucket et ses sous-buckets.
    # TODO: Ce n'est pas plustôt un sous-bucket que l'on donne ?
    """

    # Note du 19/08/2021 depuis que l'on a ajouté le bucket à 0 dans les buckets,
    # plus besoin de regarder spécifiquement le cas du 0
    if bucket.get("nb_foyer"):
        nbgens = sum(bucket["nb_foyer"].values())
    elif bucket.get("count"):
        nbgens = bucket["count"]
    else:
        raise Exception("Invalid input format: no nb_foyer or count !")
    randinnbgens = random.random() * nbgens

    # Générer un rk à partir de cette distrib (Monte-Carlo probablement)
    sommepass = 0  # nombre de foyer dans les buckets déjà dépassés. Quand on a passé le nombre de gens qu'on veut, on a fini de générer !
    for bucket_var in bucket["buckets"]:
        sommepass += bucket_var["bucket_count"]
        if sommepass > randinnbgens:
            if debug:
                print(
                    f'{sommepass} > {randinnbgens} => return {bucket_var["bucket_mean"]}'
                )
            return bucket_var["bucket_mean"]
    print("ERROR returned nothing !")


def vectorize_monte_carlo_simulation(buckets, debug=False, sample_size=1):
    initial_sample_size = sample_size
    sample = pd.DataFrame()
    while sample_size > 0:
        i = choice(buckets.index, size=1)
        sample_i = buckets.iloc[i].copy()
        weight = min(int(sample_i.bucket_count.iloc[0]), sample_size)
        sample_size = sample_size - weight
        if max(0, int(sample_i.bucket_count.iloc[0]) - weight) == 0:
            buckets = buckets.drop(i)
            buckets = buckets.reset_index(drop=True)
        else:
            buckets.loc[int(i), "bucket_count"] = max(
                0, int(sample_i.bucket_count.iloc[0]) - weight
            )
        sample_i.bucket_count = weight
        sample = pd.concat([sample, sample_i[["bucket_count", "bucket_mean"]]])

    assert (
        sample.bucket_count.sum() == initial_sample_size
    ), f"Initial sample size {initial_sample_size} differ from size of sample {sample.bucket_count.sum()} "
    sample_mean = (
        sum(sample.bucket_count * sample.bucket_mean) / sample.bucket_count.sum()
    )
    return round(sample_mean), buckets


def eval_error(sub_buckets, predict: pd.DataFrame, debug=False) -> float:
    """
    Fonction d'évaluation de l'écart entre le résultat obtenu et le résultat attendu.
    On utilise les données de chaque sous bucket pour calculer une erreur au niveau du bucket.
    ::dataset:: Le DataFrame de VAR_REF que l'on souhaite analyser
    ::predict:: Le DataFrame des données générées
    """
    # On commence par générer les sous-buckets des données
    # Cela nous donnera des chiffres à comparer
    # On ne peut pas utiliser get_calib car on ne peut pas toujours trouver le même nombre de bucket
    # Idéalement il faudrait propager un paramètre jusqu'à get_frontiere pour forcer les mêmes frontières
    # mc_subbuckets = get_calib(pandas_to_vaex(predict), predict.columns[0], nb_bucket_asked)['buckets']
    values = sorted(predict[predict.columns[0]].to_list())
    mc_subbuckets = []
    y_test_mean, y_pred_mean = [], []
    # tc.assertTrue(isinstance(sub_buckets, list))
    if not isinstance(sub_buckets, list):
        if debug:
            print(f"WARNING - The bucket is not a list : {sub_buckets}")
        return 1.0
    sum_mean_pred = 0
    sum_mean_test = 0
    for bucket in sub_buckets:
        tc.assertIsNotNone(bucket.get("bucket_count"))
        # fin = debut + bucket['bucket_count']
        # On prend les foyers dans la tranche de var
        extrait = [
            v for v in values if bucket["lower_bound"] < v <= bucket["upper_bound"]
        ]
        buck = {
            "bucket_count": len(extrait),  # N'a pas d'intérêt
            "bucket_sum": sum(extrait),
            "bucket_mean": 0 if len(extrait) == 0 else sum(extrait) / len(extrait),
        }

        mc_subbuckets.append(buck)
        # tc.assertEqual(len(extrait), bucket['bucket_count'])
        #         tc.assertEqual(sum(extrait), bucket['bucket_sum'])
        #         tc.assertEqual(0 if len(extrait) == 0 else sum(extrait)/ len(extrait), bucket['bucket_mean'])

        # On donnera ensuite ces valeurs à Scikit-Learn pour qu'il calcul l'erreur
        sum_mean_pred += buck["bucket_mean"]
        sum_mean_test += bucket["bucket_mean"]
        y_test_mean.append(bucket["bucket_mean"])
        y_pred_mean.append(buck["bucket_mean"])
        # La somme n'a pas de sens car POTE et ERFS n'ont pas la même taille
    #         y_test_sum.append(bucket['bucket_sum'])
    #         y_pred_sum.append(buck['bucket_sum'])
    tc.assertEqual(len(sub_buckets), len(mc_subbuckets))
    mean_pred = sum_mean_pred / len(sub_buckets)
    mean_test = sum_mean_test / len(sub_buckets)
    # On utilise la métrique mean_absolute_percentage_error qui est indépendante de la dimension des variables (une erreur entre 1 et 2 est la même qu'entre 1000 et 2000)
    # mean_squared_log_error : this metric penalizes an under-predicted estimate greater than an over-predicted estimate.
    # mean_squared_error : Pas satisfaisant car dépend de l'empleur des valeurs
    err_mean = mean_absolute_percentage_error(y_test_mean, y_pred_mean)
    err_all_sub_bucket_mean = mean_absolute_percentage_error(
        [mean_test, mean_test], [mean_pred, mean_pred]
    )
    if debug:
        print(f"{mean_test} {mean_pred} => error : {err_all_sub_bucket_mean}")
    # r2_sum = r2_score(y_test_sum,y_pred_sum)
    errors = [err_mean, err_all_sub_bucket_mean]
    error = sum(errors) / len(errors)

    if debug:
        print(f"{err_mean} {err_all_sub_bucket_mean} => error : {error}")
    # On soustrait l'erreur à 1 pour avoir un comportement "lower is better"
    # A noter que l'erreur R2 peut être négative
    return error


def force_mean_with_factor(
    sub_buckets, df_target, col_name="monte_carlo_fake_var", debug=False
):
    """
    On calcul la moyenne du dataframe, on calcul ensuite le ration qui va permettre
    de corriger les valeurs pour obtenir la moyenne du bucket.
    ::bucket:: Le bucket dont on veut s'approcher de la moyenne
    ::df_target:: Le DataFrame contenant les données
    ::col_name:: Le nom de la colonne à corriger
    ::return:: Le datframe d'entrée modifié
    """
    df_result = df_target.copy()
    for bucket in sub_buckets:
        inf = bucket["lower_bound"]  # noqa: F841
        supp = bucket["upper_bound"]  # noqa: F841
        buck_mean = bucket["bucket_mean"]
        df_bucket = df_target.query("@inf <= " + col_name + " < @supp").copy()
        df_mean = df_bucket[col_name].mean()
        factor = buck_mean / df_mean
        df_bucket[col_name] = df_bucket[col_name] * factor
        df_result.update(df_bucket[[col_name]])
        if debug:
            print(
                f"Mean before {df_mean}, mean after : {df_bucket[col_name].mean()} {buck_mean} {factor}"
            )
    return df_result


def apply_Monte_Carlo(
    df: pd.DataFrame,
    copules: dict,
    bucket_level_col_name="revkire",
    by_quantile=True,
    out_col="monte_carlo_fake_var",
    weight_var=None,
    nb_tirage=1,
    seed=None,
    use_force_mean_with_factor=False,
    debug=False,
) -> pd.DataFrame:
    """
    Applique la méthode de Monte-Carlo a un jeux de données
    ::df:: Le dataframe auquel injecter les données
    ::copules:: Le dictionnaire de copule complet
    ::bucket_level_col_name:: Le nom de la colonne utilisée pour calculer le bucket principal.
    ::out_col:: Le nom de la colonne en sortie pour le résultat de la méthode de Monte-Carlo
    ::nb_tirage:: Nombre de tirages aléatoires pour chaque bucket
    """
    final_df = pd.DataFrame()
    df_best_result = None
    # Set the seed to have reproductible results
    seed = int(time()) if seed is None else seed
    random.seed(seed)
    errors = []
    print(f"Seed used : {seed}")
    # On vérifie que l'on est au bon niveau
    if not isinstance(copules, list):
        if copules.get("copules"):
            copules = copules["copules"]
    tc.assertIsNotNone(copules[0].get("buckets"))
    j = 0
    np.random.seed(seed)
    df["rand"] = np.random.random(len(df))
    df = df.sort_values("rand")
    for bucket in tqdm(copules):
        j += 1
        min_error = 1e99
        seuil_inf = bucket["lower_bound"]  # noqa: F841
        seuil_supp = bucket["upper_bound"]  # noqa: F841
        if by_quantile:
            df_bucket = df.query("quantiles == @j").copy()
        else:
            df_bucket = df.query(
                f"@seuil_inf <= {bucket_level_col_name} < @seuil_supp"
            ).copy()
        # si secret statistique on impute une valeur null pour tout le quantile
        if bucket["buckets"] == "NO_DETAIL_TO_PRESERVE_SECRET":
            df_bucket["monte_carlo_fake_var"] = df_bucket[weight_var] * 0
            final_df = pd.concat([final_df, df_bucket])
            df_best_result = None
        # On fait nb_tirage simulation de Monte-Carlo
        else:
            for i in range(nb_tirage):
                if weight_var is None:
                    serie = df_bucket[bucket_level_col_name].apply(
                        lambda rfr: monte_carlo_simulation(bucket)
                    )
                else:
                    if bucket.get("count_nonzero"):
                        nonzero = bucket["count_nonzero"]  # noqa: F841
                    if bucket.get("nb_foyer"):
                        nonzero = bucket["nb_foyer"]["nonzero"]  # noqa: F841
                    df_bucket["cumsum"] = df_bucket[weight_var].cumsum()
                    df_bucket_pos = df_bucket.query("cumsum <= @nonzero").copy()
                    df_bucket_nonpos = df_bucket.query("cumsum > @nonzero").copy()
                    if not df_bucket_pos.empty:
                        df_bucket_pos["serie"] = 0
                        serie = list()
                        buckets = pd.DataFrame(bucket["buckets"])
                        buckets["bucket_count"] = np.ceil(
                            buckets["bucket_count"] * 1.05
                        )
                        if buckets.iloc[0].bucket_sum == 0:
                            buckets = buckets.iloc[1:]
                            buckets = buckets.reset_index(drop=True)
                        for i in df_bucket_pos.index:
                            serie_i, buckets = vectorize_monte_carlo_simulation(
                                buckets, sample_size=int(df_bucket_pos[weight_var][i])
                            )
                            df_bucket_pos.loc[int(i), "serie"] = serie_i
                        # serie = df_bucket_pos[weight_var].apply(
                        #     lambda w: vectorize_monte_carlo_simulation(
                        #         bucket, sample_size=w
                        #     )
                        # )
                        # print(df_bucket_pos['serie'])
                        if not df_bucket_nonpos.empty:
                            serie = pd.concat(
                                [
                                    df_bucket_pos["serie"],
                                    df_bucket_nonpos[weight_var] * 0,
                                ]
                            )
                    else:
                        serie = df_bucket_nonpos[weight_var] * 0
                df_tmp = pd.DataFrame({f"monte_carlo_fake_var_{i}": serie})
                error = eval_error(bucket["buckets"], df_tmp)
                if error < min_error:
                    min_error = error
                    df_bucket["monte_carlo_fake_var"] = df_tmp[
                        f"monte_carlo_fake_var_{i}"
                    ]
                    df_best_result = df_bucket
            errors.append(min_error)
            # On conserve le meilleur résultat
            if df_best_result is None:
                print("WARNING : apply_Monte_Carlo did not work")
                df_bucket["monte_carlo_fake_var"] = 0
                df_best_result = df_bucket
            if use_force_mean_with_factor:
                df_best_result = force_mean_with_factor(
                    bucket["buckets"], df_best_result, col_name="monte_carlo_fake_var"
                )
                error = eval_error(bucket["buckets"], df_best_result)
                if debug:
                    print(f"error after {error}")

            # final_df = final_df.append(df_best_result)
            final_df = pd.concat([final_df, df_best_result])
            df_best_result = None
    tc.assertEqual(len(final_df), len(df))
    df[out_col] = final_df["monte_carlo_fake_var"].fillna(0)
    df.drop(columns=["rand"], inplace=True)
    df = df.sort_index()
    return df, errors


def integration_data_ff(sample_pop_ff, data_to_process, nb_tirage):
    for data in data_to_process:
        # On charge les copules
        with open(config.get("COPULES") + data["file"]) as fichier:
            dict_copules_RFR_Data = json.load(fichier)
        print(
            f"Nombre de bucket : {len(dict_copules_RFR_Data)} Nombre de sous-bucket : {len(dict_copules_RFR_Data[1]['buckets'])}"
        )
        # Chercher la distribution optimale
        # On ajoute une distribution de data dans notre échantillon de population
        # Pour chaque ligne de l'ERFS-FPR on appel calcul_distrib_from_copules en lui donnant le RFR de la ligne en cours.
        df, errors = apply_Monte_Carlo(
            df=sample_pop_ff,
            copules=dict_copules_RFR_Data,
            bucket_level_col_name="rfr",
            out_col=data["column_name"],
            nb_tirage=nb_tirage,
            # seed = 25,
            use_force_mean_with_factor=True,
            debug=True,
        )

    return sample_pop_ff, data_to_process
