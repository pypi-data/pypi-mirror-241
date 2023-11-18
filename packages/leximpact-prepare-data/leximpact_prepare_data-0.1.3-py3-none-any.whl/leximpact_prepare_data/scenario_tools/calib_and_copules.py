import copy
import gc
import random
import statistics
import unittest
from copy import deepcopy
from statistics import mean, stdev
from time import time
from typing import Dict, List, Union

import pandas as pd
import vaex
from ruamel.yaml.comments import CommentedSeq

tc = unittest.TestCase()


class DatasetNotSorted(Exception):
    pass


class SecretViolation(Exception):
    pass


SECRET_VIOLATION = "SECRET_VIOLATION"
SECRET_KEEPED = "NO_DETAIL_TO_PRESERVE_SECRET"


def get_borders(
    dataset_size: int,
    nb_bucket: int,
    add_upper_bucket=[0.1, 1e-2],  # [0.1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6],
    minimal_bucket_size=12,
    debug=False,
) -> List:
    """
    Compute the bins for a given dataset length.
    Arg:
        dataset_size
    Return:
        A List of index to split the data to get the bins.
    """
    # Si nous n'avons pas assez de personnes au dessus de zéro, on arrête là.
    if dataset_size < minimal_bucket_size:
        print(
            f"WARNING get_borders, moins de {minimal_bucket_size} éléments => On retourne une liste vide. !!!!!!!!!!"
        )
        return []

    # Si nous savons déjà qu'on n'a pas assez de foyer pour remplir les bucket demandés, on fait moins de bucket
    nb_bucket = min(dataset_size // minimal_bucket_size, nb_bucket)
    # S'il ne reste qu'un bucket, on le retourne
    if nb_bucket == 1:
        return [dataset_size]

    # On génère les frontières de base
    frontieres = [int(dataset_size * i / nb_bucket) for i in range(1, nb_bucket)]
    if debug:
        print("get_borders frontieres de base", frontieres)
    # On ajoute des frontières supérieure
    for r in add_upper_bucket:
        nouvelle_frontiere = int(dataset_size * r)
        if (
            nouvelle_frontiere < (dataset_size - frontieres[-1])
            and dataset_size - nouvelle_frontiere < dataset_size
        ):
            frontieres += [dataset_size - nouvelle_frontiere]

    # On ajoute la frontière supérieure
    frontieres += [dataset_size]
    if debug:
        print("get_borders frontieres avant", frontieres)
    if debug:
        print("get_borders len(borders) avant", len(frontieres))
    # On retire les sous-buckets de moins de 12 personnes
    # Comment est-ce que ça peut encore arriver puisqu'on prend un nombre fixe de personne ?
    # Car nous avons des buckets inégales type [12,11,12] et surtout ceux que l'on ajoute à la fin.
    i = 0
    while i < len(frontieres) - 1:
        ecart_avec_front_supp = frontieres[i + 1] - frontieres[i]
        # Si on a moins de 12 personnes d'écart entre 2 frontières,
        if ecart_avec_front_supp < minimal_bucket_size:
            # On supprime une frontière pour combiner les 2 buckets mitoyens
            if (  # Si la première fontière repecte le secret
                (i == 0 and frontieres[i] >= minimal_bucket_size)
                or (  # Ou que la frontère précédente le respecte
                    i > 0 and frontieres[i] - frontieres[i - 1] >= minimal_bucket_size
                )
                # Et que nous ne sommes pas à la fin
            ) and (i + 1 < len(frontieres) - 1):
                # Alors on supprime la frontière suivante
                if debug:
                    print(
                        f"get_borders On supprime la frontière i+1 {i+1} pour combiner les 2 buckets mitoyens : borders[i]={frontieres[i]}, borders[i+1]={frontieres[i+1]} , borders[i+2]={frontieres[i+2]}"
                    )
                frontieres = frontieres[: i + 1] + frontieres[i + 2 :]
                # Sinon on supprime la frontière actuelle
            else:
                if debug:
                    print(
                        f"get_borders On supprime la frontière i {i} pour combiner les 2 buckets mitoyens : borders[i]={frontieres[i]}, borders[i+1]={frontieres[i+1]} "
                    )
                frontieres = frontieres[:i] + frontieres[i + 1 :]
        else:
            i += 1
    if debug:
        print("get_borders frontieres apres", frontieres)
    if len(frontieres) == 0:
        if dataset_size > minimal_bucket_size:
            return [dataset_size]
        else:
            print("ERROR get_borders : On ne devrait jamais arriver ici !")
            return []
    if len(frontieres) == 1:
        if frontieres[0] > minimal_bucket_size:
            return [dataset_size]
        else:
            print(
                "ERROR get_borders : On ne devrait jamais arriver ici ! Voici les frontières",
                frontieres,
            )
            return []
    if debug:
        print("get_borders frontieres avant fin", frontieres)
    # On ajoute la dernière frontière si nécessaire
    if (len(frontieres) > 0) and (frontieres[-1] != dataset_size):
        # frontieres += [dataset_size]
        print(
            "ERROR get_borders : On ne devrait jamais arriver ici ! Voici les frontières",
            frontieres,
        )
        return []

    return frontieres


def enforce_secret(
    data: dict, nbzero: int, nb_above_zero: int, minimal_bucket_size: int = 12
) -> None:
    """
    Make sure that we do not give info about entity number when they are below minimal_bucket_size
    """
    if nbzero + nb_above_zero < minimal_bucket_size:
        raise SecretViolation()
    count_zero = (
        nbzero if nbzero >= minimal_bucket_size or nbzero == 0 else SECRET_KEEPED
    )
    count_nonzero = (
        nb_above_zero
        if nb_above_zero >= minimal_bucket_size or nb_above_zero == 0
        else SECRET_KEEPED
    )
    if SECRET_KEEPED in [count_zero, count_nonzero]:
        data["count_zero"] = SECRET_KEEPED
        data["count_nonzero"] = SECRET_KEEPED
    else:
        data["count_zero"] = count_zero
        data["count_nonzero"] = count_nonzero


def sanitize_bucket(buckets):
    """
    Verify bucket and re-compute upper and lower bound to ensure continuous borders.
    """
    if buckets == SECRET_VIOLATION:
        raise SecretViolation("SECRET STATISTIQUE > 0.85 NON RESPECTE")

    # Sanity check
    for b in buckets:
        if b == SECRET_VIOLATION:
            raise SecretViolation("SECRET STATISTIQUE > 0.85 NON RESPECTE")
    # Remove empty bucket
    buckets = [b for b in buckets if b["bucket_count"] != 0]
    if len(buckets) < 2:
        return buckets
    prev_b = buckets[0]
    for b in buckets[1:]:
        if b["lower_bound"] > b["upper_bound"]:
            print(b)
            raise DatasetNotSorted(
                "The resuling buckets are not sorted: lower_bound > upper_bound!"
            )
        if prev_b["lower_bound"] > b["lower_bound"]:
            if (prev_b["lower_bound"] == 0 and prev_b["upper_bound"] == 0) and b[
                "lower_bound"
            ] < 0:
                # prev_b is the zero bucket
                pass
            else:
                print(prev_b)
                print(b)
                raise DatasetNotSorted(
                    "The resuling buckets are not sorted prev lower_bound > lower_bound!"
                )
        if prev_b["upper_bound"] > b["lower_bound"]:
            if (prev_b["lower_bound"] == 0 and prev_b["upper_bound"] == 0) and b[
                "lower_bound"
            ] < 0:
                # prev_b is the zero bucket
                pass
            else:
                print(prev_b)
                print(b)
                raise DatasetNotSorted(
                    "The resuling buckets are not sorted prev upper_bound > lower_bound!"
                )
        if prev_b["upper_bound"] < b["lower_bound"]:
            # We will compute the middle to have continuous bucket
            prev_b["upper_bound"] = (
                prev_b["upper_bound"] + (b["lower_bound"] - prev_b["upper_bound"]) / 2
            )
            b["lower_bound"] = prev_b["upper_bound"]
        prev_b = b
    return buckets


class Quantile:
    def __init__(
        self, variable_values: List, minimal_bucket_size: int = 12, debug: bool = False
    ):
        self.debug = debug
        variable_values.sort()
        self.variable_values = variable_values
        self.lower_bound = variable_values[0]
        self.upper_bound = variable_values[-1]
        self.elements_count = len(variable_values)
        self.nbnz = len(variable_values)
        self.nbzero = sum(1 for el in variable_values if el < 1)
        self.sum_variable = sum(variable_values)
        self.minimal_bucket_size = minimal_bucket_size

    """
    Pour des frontières données va générer les quantiles correspondants
    """

    def get_quantile(self, nb_bins: int = 10):
        self.borders = get_borders(
            self.elements_count, nb_bucket=nb_bins, add_upper_bucket=[], debug=False
        )
        # Si nous n'avons pas assez d'éléments
        if len(
            self.borders
        ) < nb_bins or self.elements_count < self.minimal_bucket_size * len(
            self.borders
        ):
            raise SecretViolation(
                f"Quantile : ERROR !!!!, moins de {self.minimal_bucket_size} éléments par bucket."
            )
        self.quantile_from_borders()
        return self.to_dict()

    def quantile_from_borders(self, borders: List = None, compute_pareto=False):
        """
        Arg:
            borders: Borders to split on.
            compute_pareto: If you want pareto in output.
        """
        if not borders:
            borders = self.borders
        variable_values = self.variable_values
        if self.debug:
            print(f"Quantile on borders {len(borders)}")

        # Si nous n'avons pas assez de personnes au dessus de zéro, on arrête là.
        if self.elements_count < self.minimal_bucket_size * len(borders):
            raise SecretViolation(
                f"Quantile : ERROR !!!!, moins de {self.minimal_bucket_size} éléments par bucket."
            )

        lower_index = 0
        buckets = []
        for quantile_index, upper_index in enumerate(borders):
            current_values = variable_values[lower_index:upper_index]
            lower_bound = current_values[0]
            upper_bound = current_values[-1]
            sum_var_bucket = sum(current_values)
            if compute_pareto:
                if upper_index == self.elements_count:
                    values_above = []
                    count_above_upper_bound = 0
                    sum_above_upper_bound = 0
                    ratio_count_above_upper_bound = 0
                    mean_above_upper_bound = 0
                else:
                    values_above = variable_values[upper_index:]
                    count_above_upper_bound = len(values_above)
                    sum_above_upper_bound = sum(values_above)
                    ratio_count_above_upper_bound = len(values_above) / len(
                        current_values
                    )
                    mean_above_upper_bound = mean(values_above)
            tranche_courante = {
                "quantile_index": quantile_index,
                "lower_bound": lower_bound,
                "upper_bound": upper_bound,
                "bucket_count": len(current_values),
                "bucket_sum": sum(current_values),
                "bucket_mean": mean(current_values),
                "bucket_stdev": stdev(current_values),
            }
            if compute_pareto:
                tranche_courante["count_above_upper_bound"] = count_above_upper_bound
                tranche_courante["sum_above_upper_bound"] = sum_above_upper_bound
                tranche_courante[
                    "ratio_count_above_upper_bound"
                ] = ratio_count_above_upper_bound
                tranche_courante["mean_above_upper_bound"] = mean_above_upper_bound

            lower_index = upper_index
            max_ff_bucket = max(current_values)
            # Vérification que la personne la plus riche du bucket ne représente pas plus de 85% du bucket
            if (
                sum_var_bucket > 0
                and (max_ff_bucket / (sum_var_bucket - max_ff_bucket)) > 0.850
            ):
                raise SecretViolation(
                    f"Quantile : ERROR SECRET STATISTIQUE > 0.85 NON RESPECTE (ratio={max_ff_bucket / (sum_var_bucket-max_ff_bucket):.3f})"
                )
            buckets.append(tranche_courante.copy())
        buckets = sanitize_bucket(buckets)
        # On sauvegarde la distribution de ce bucket
        self.buckets = buckets

    def to_dict(self):
        """
        Exporte le résultat dans un dictionnaire Python
        """
        d = {
            "lower_bound": self.lower_bound,
            "upper_bound": self.upper_bound,
            "sum": self.sum_variable,
            "count": self.nbzero + self.nbnz,
            "count_zero": "whatever",
            "count_nonzero": "whatever",
            "buckets": self.buckets,
        }
        enforce_secret(d, self.nbzero, self.nbnz, self.minimal_bucket_size)
        return d


list_revenus_each_bucket = [[]]
frontieres_valeurs = None


def get_primary_buckets(
    vdx_sort: vaex.dataframe.DataFrameLocal,
    nb_bucket: int,
    variable_to_split_on: str = "revkire",
    minimal_bucket_size=12,
    add_upper_bucket=[0.1, 1e-2],
    debug=False,
) -> Dict:
    """
    Objectif: Split the variable in buckets
    Dans chaque bucket on stocke toutes les valeurs non nulles de "variable"
    ::vdx_sort:: Le dataset, trié selon la variable à étudier
    ::nb_bucket:: Nombre de tranches souhaitées
    ::variable_to_split_on:: Variable on which to split buckets
    ::debug:: Pour activer un mode debug, qui affiche des traces
    """
    dataset_size = vdx_sort.shape[0]  # Nb de lignes
    # Conversion en array
    variable_array = vdx_sort.to_arrays(
        column_names=[variable_to_split_on], selection=False, array_type="python"
    )[0]
    # On vérifie que le dataset est bien trié
    previous = variable_array[-1]
    for i in range(1, 1000):
        idx = dataset_size // i
        idx = idx if idx != dataset_size else dataset_size - 1
        if previous < variable_array[idx]:
            raise DatasetNotSorted(
                f"Your dataset is not sorted on {variable_to_split_on}!"
            )
        previous = variable_array[idx]

    # Découpage du RFR en buckets:
    borders = get_borders(
        dataset_size=dataset_size,
        nb_bucket=nb_bucket,
        minimal_bucket_size=minimal_bucket_size,
        add_upper_bucket=add_upper_bucket,
        debug=debug,
    )

    # On retire la dernière frontière pour éviter des tests (index out of range), on la remetra après
    borders = borders[:-1]
    i = 0
    # On supprime les frontières qui n'auraient que du 0
    while i < len(borders):
        if variable_array[borders[i]] < 1:
            if debug:
                print(
                    f"WARNING: On efface la frontière d'index {i} : {borders[i]} inutile car valeur de la borne haute est {variable_array[borders[i]]}"
                )
            borders = borders[:i] + borders[i + 1 :]
        else:
            i += 1
    frontieres_valeurs = [0] + [variable_array[frontiere] for frontiere in borders]
    # On ajoute une valeur de fin trés haute (10^15€)
    frontieres_valeurs += [10**15]
    # On remet la dernière frontière
    borders += [dataset_size]
    dic = {"borders_values": frontieres_valeurs, "borders": borders}
    del variable_array
    gc.collect()
    return dic


def get_copulas(
    vdf: vaex.dataframe.DataFrameLocal,
    primary_variable: str,
    variable: str,
    nb_bucket_var: int,
    primary_buckets: List,
    add_upper_bucket=[0.1, 1e-2],
    debug=False,
    minimal_bucket_size=12,
):
    """
    On nous donne des tranches de RFR, en nombre de personne, et en valeur de RFR
    Pour chacune de ses tranches on doit extraire les valeurs de 'variable'
    On ne garde que celle supérieure à 0 et on les envoie à DistribDeVarVaex
    ::vdf:: Le jeux de données
    ::variable:: Nom de la variable secondaire.
    ::nb_bucket_var:: Nombre de tranches de variable secondaire souhaités.
    ::primary_buckets:: La liste des tranches de RFR.
    ::debug:: Pour activer un mode debug, qui affiche des traces.
    ::minimal_bucket_size:: Nombre minimal d'individus pour respecter le secret statistique.
    """
    controle = []
    copules = []
    frontieres_valeurs = primary_buckets["borders_values"]
    borders = primary_buckets["borders"]

    if primary_variable in vdf.get_column_names():
        primary_variable = primary_variable
    else:
        primary_variable = vdf.get_column_names()[0]

    # Conversion en array
    primary_variable_array = vdf.to_arrays(
        column_names=[primary_variable], selection=False, array_type="python"
    )[0]
    dataset_size = len(primary_variable_array)
    # On vérifie que le dataset est bien trié
    previous = primary_variable_array[-1]
    for i in range(1, 1000):
        idx = dataset_size // i
        idx = idx if idx != dataset_size else dataset_size - 1
        if previous < primary_variable_array[idx]:
            raise DatasetNotSorted(f"Your dataset is not sorted on {primary_variable}!")
        previous = primary_variable_array[idx]

    # On parcourt les frontières de FF (= les index dans le tableau)
    idx_inf = 0

    debut = time()
    # On ne peut malheureusement pas filtrer par > 0 avant extraction car cela fausserait le nombre de valeur
    variable_all_values = vdf.to_arrays(
        column_names=[variable], selection=False, array_type="python"
    )[0]

    # On fait l'hypothèse que c'est bien trié par ordre croissant
    lower_bound = primary_variable_array[idx_inf]
    if debug:
        print(f"Temps d'extraction par to_arrays  {time()-debut}")
    for i, idx_sup in enumerate(borders):
        starttime = time()
        upper_bound = frontieres_valeurs[i + 1]  # Car frontieres_valeurs contient 0
        variable_values = variable_all_values[idx_inf:idx_sup]
        # nb_entity = vdf_tmp.shape[0]
        nb_entity = len(variable_values)
        if debug:
            print(f"-----------------Temps après slice {time()-starttime}")
        assert nb_entity == idx_sup - idx_inf
        # Quand il y a beaucoup de personne ayant le même revenu on peut avec des tranches avec lower_bound=upper_bound, mais ce n'est pas gênant
        if (
            primary_variable_array[idx_inf] != lower_bound
            and lower_bound != upper_bound
        ):
            print(
                f"get_copulas {i} WARNING: Il y a peut-être un problème car le RFR du premier index (idx_inf={idx_inf}) est {primary_variable_array[idx_inf]} alors que lower_bound vaut {lower_bound}"
            )
        if (
            i != len(borders) - 1
            and primary_variable_array[idx_sup] != upper_bound
            and lower_bound != upper_bound
        ):
            print(
                f"get_copulas {i} WARNING: Il y a peut-être un problème car le RFR du dernier index (idx_sup={idx_sup}) est {primary_variable_array[idx_sup]} alors que upper_bound vaut {upper_bound}"
            )
        # Remove 0
        variable_values = [v for v in variable_values if (v < -0.9999 or v > 0.1)]

        if debug:
            print(f"Temps avant sort {time()-starttime}")
        # Tri des variables : sort() est plus rapide que sorted, mais écrase notre liste
        variable_values.sort()
        # variable_values = sorted(variable_values)
        if debug:
            print(f"Temps après sort {time()-starttime}")
        if debug:
            print(
                f"get_copulas {i} : index entre idx_inf={idx_inf} et idx_sup={idx_sup} - RFR entre lower_bound={lower_bound} et upper_bound={upper_bound} - {len(variable_values)} valeurs différentes de zéro."
            )
            if len(variable_values) > 0:
                print(
                    f"\tmin(variable_values)={min(variable_values)} max(variable_values)={max(variable_values)}"
                )
        if len(variable_values) > idx_sup - idx_inf:
            print(
                f"get_copulas ERROR i={i} len(variable_values)={len(variable_values)} != {idx_sup - idx_inf}"
            )
        assert len(variable_values) <= (idx_sup - idx_inf)
        if debug:
            DistribDeVar_time = time()
        bdr = DistribDeVarVaex(
            variable_values=variable_values,
            variable=variable,
            nb_entity=nb_entity,
            nb_bucket_var=nb_bucket_var,
            lower_bound=lower_bound,
            upper_bound=upper_bound,
            add_upper_bucket=add_upper_bucket,
            debug=debug,
            minimal_bucket_size=minimal_bucket_size,
        )
        if debug:
            print(f"Temps de DistribDeVarVaex {time()-DistribDeVar_time}")
        # Et on ajoute ce tableau à la liste des tableaux
        copules += [bdr.to_dict()]

        idx_inf = idx_sup
        lower_bound = upper_bound
        if debug:
            print(f"Temps après fin de la boucle {time()-starttime} --------------")
        if debug and i > 10:
            print("DEBUG EXIT !!!")
            break
    dico = {"controle": controle, "copules": copules}

    return dico


class DistribDeVarVaex:
    """
    On créée une classe qui, pour un bucket de RFR donné [lower_bound, upper_bound], va générer la distribution des Rk (ou autre Variable) de ce bucket (que l'on a dans liste_des_rk).
    Cette distribution est retournée sous la forme:
        resultat = [ [Nb de gens1,Somme des Rk 1],[Nb2, Sum2], [], ... , [Nb N, Sum N]]
            avec N le nb de buckets de Rk
    """

    def __init__(
        self,
        variable_values: List,
        variable: str,
        nb_entity: int,
        nb_bucket_var=10,
        lower_bound=0,
        upper_bound=10 ^ 15,
        minimal_bucket_size=12,
        add_upper_bucket=[0.1, 1e-2],
        debug=False,
    ):
        """
        Arg:
            variable_values:: Liste de toutes les valeurs de la variable secondaire, dajà triée par ordre croissant.
            variable:: Nom de la variable secondaire.
            nb_entity:: Nombre de foyers fiscaux dans cette tranche de la variable secondaire.
            nb_bucket_var:: Nombre de tranche souhaité.
            lower_bound:: Borne inférieure de RFR.
            upper_bound:: Borne supérieure de RFR.
            debug:: Pour activer un mode debug, qui affiche des traces
        """
        if debug:
            print(f"DistribDeVarVaex - RFR entre {lower_bound} et {upper_bound}")
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.elements_count = nb_entity
        self.nbnz = len(variable_values)
        self.nbzero = max(self.elements_count - self.nbnz, 0)
        self.sum_variable = sum(variable_values)
        self.minimal_bucket_size = minimal_bucket_size
        default_tranche = {
            "lower_bound": 0,
            "upper_bound": 0,
            "bucket_count": 0,
            "bucket_sum": 0,
            "bucket_mean": 0,
            "bucket_stdev": 0,
            "count_above_upper_bound": 0,
            "sum_above_upper_bound": 0,
            "ratio_count_above_upper_bound": 0,
            "mean_above_upper_bound": 0,
        }
        # Si nous n'avons pas assez de personnes à zéro, on doit arrêter là.
        # Instead we would have to not disclose the total number of entity
        self.mask_total_number_of_entity = False
        if self.nbzero != 0 and self.nbzero < minimal_bucket_size:
            self.mask_total_number_of_entity = True
            print(
                f"DistribDeVar : less than {minimal_bucket_size} for zero elements. {self.nbzero} elements at 0"
            )
            # raise SecretViolation(
            #     f"DistribDeVar : less than {minimal_bucket_size} for zero elements."
            # )
        # Si nous n'avons pas assez de personnes au dessus de zéro, on arrête là.
        if nb_entity < minimal_bucket_size:
            raise SecretViolation(
                f"DistribDeVar : less than {minimal_bucket_size} elements. {self.nbzero} elements at 0"
            )
        # Non fatal error more than minimal_bucket_size elements
        if self.nbnz < minimal_bucket_size:
            print(
                f"DistribDeVar : less than {minimal_bucket_size} for non_zero elements. {self.nbzero} elements at 0"
            )
            self.buckets = SECRET_KEEPED
            return

        # On vérifie que le dataset est bien trié
        dataset_size = len(variable_values)
        previous = variable_values[dataset_size - 1]
        for i in range(1, 100):
            idx = dataset_size // i
            idx = idx if idx != dataset_size else dataset_size - 1
            # < because we iterate from the end with idx = dataset_size // i
            if previous < variable_values[idx]:
                raise DatasetNotSorted(
                    f"Your dataset is not sorted on {variable}! i={i} idx={idx},  variable_values[idx]={variable_values[idx]} >= previous={previous}"
                )
            previous = variable_values[idx]

        premiere_tranche = {
            "lower_bound": 0,
            "upper_bound": 0,
            "bucket_count": self.nbzero
            if self.nbzero >= minimal_bucket_size or self.nbzero == 0
            else SECRET_KEEPED,
            "bucket_sum": 0,
            "bucket_mean": 0,
            "bucket_stdev": 0,
            "count_above_upper_bound": self.nbnz,
            "sum_above_upper_bound": self.sum_variable,
            "ratio_count_above_upper_bound": self.nbnz / self.elements_count,
            "mean_above_upper_bound": self.sum_variable / self.nbnz,
        }
        secret_statistique_respecte = True
        while nb_bucket_var > 0:
            # On récupère les frontières avec add_upper_bucket et nb_bucket_var qui peuvent diminuer
            # si on ne respecte pas le secrect statistique
            self.borders = get_borders(
                dataset_size=self.nbnz,
                nb_bucket=nb_bucket_var,
                add_upper_bucket=add_upper_bucket,
                minimal_bucket_size=minimal_bucket_size,
                debug=debug,
            )
            if debug:
                print("borders:", self.borders)

            if self.borders == []:
                raise ValueError("ERROR Borders are empty ! nb_bucket={nb_bucket}")

            # Calcul de la distribution dans ces buckets
            currbuck = 0
            # The first bucket is the one with value==0
            buckets = [premiere_tranche]
            max_ff_bucket = 0
            sum_var_bucket = 0
            tranche_courante = deepcopy(default_tranche)
            values = []
            # On parcourt les var !=0
            for idrk, current_value in enumerate(variable_values):
                #                 if debug:
                #                     print(f"idrk={idrk}, current_value={current_value} tranche_courante:{tranche_courante}, filtered_above_seuil:{self.rknonzero[idrk:]}")
                # Si on est dans la première itération d'un nouveau bucket
                if tranche_courante["bucket_count"] == 0:
                    tranche_courante["lower_bound"] = current_value

                # Si le nb d'observations est supérieur au plafond du current bucket,
                # On est à la fin du bucket
                if (
                    idrk >= self.borders[currbuck] or idrk == self.nbnz - 1
                ):  # or idrk==self.nbnz
                    if idrk == self.nbnz - 1:
                        # On est à la fin, donc on inclue current_value dans le bucket en cours
                        # La regle des 85% c'est  en excluant l'élément concerné dans la somme :
                        # Aucune  case  du  tableau  ne  doit  contenir  de  données  pour  lesquelles
                        # une personne représente plus de 85% du total
                        # See https://www.insee.fr/fr/statistiques/fichier/1300624/guide-secret.pdf
                        sum_var_bucket += current_value
                        values.append(current_value)
                        tranche_courante["bucket_count"] += 1
                        if current_value > max_ff_bucket:
                            max_ff_bucket = current_value
                    # Vérification que la personne la plus riche du bucket ne représente pas plus de 85%
                    if (
                        sum_var_bucket > 0
                        and max_ff_bucket / (sum_var_bucket - max_ff_bucket) > 0.85
                    ):
                        secret_statistique_respecte = False
                        # On réduit le nombre de bucket
                        if add_upper_bucket != []:
                            # On retire le ratio le plus haut
                            add_upper_bucket = add_upper_bucket[:-1]
                        else:
                            # Si on n'a plus de ratio d'affinage des hauts revenus,
                            # On réduit le nombre de bucket
                            nb_bucket_var -= 1
                        if debug:
                            print(
                                f"DistribDeVarVaex : Warning SECRET STATISTIQUE > 0.85 NON RESPECTE (idrk={idrk}), on refait une passe avec moins de frontières"
                            )
                            print(
                                f"sum_var_bucket={sum_var_bucket}, max_ff_bucket={max_ff_bucket},currbuck={currbuck}, nb_bucket_var={nb_bucket_var}, add_upper_bucket={add_upper_bucket}"
                            )
                        buckets = [SECRET_VIOLATION]
                        # On relance la boucle principale au début
                        break
                    else:
                        secret_statistique_respecte = True
                        # On calcul les metadata de notre bucket
                        tranche_courante["bucket_sum"] = sum_var_bucket
                        tranche_courante["bucket_mean"] = (
                            sum_var_bucket / tranche_courante["bucket_count"]
                        )
                        # TODO : calculer incrémentatlement l'écart-type, mais c'est compliqué https://math.stackexchange.com/questions/102978/incremental-computation-of-standard-deviation
                        # Ca permetrait de réduire l'emprunte mémoire, mais elle est acceptable : 300 000 valeurs pour des centiles.
                        if tranche_courante["bucket_count"] > 1:
                            tranche_courante["bucket_stdev"] = statistics.stdev(values)
                        # Si on n'est pas dans le dernier bucket
                        if idrk != self.nbnz - 1:
                            filtered_above_seuil = variable_values[idrk:]
                            nb_above_seuil = len(filtered_above_seuil)
                            sum_above_seuil = sum(filtered_above_seuil)
                            tranche_courante["count_above_upper_bound"] = nb_above_seuil
                            tranche_courante["sum_above_upper_bound"] = sum_above_seuil
                            if self.elements_count > 0:
                                tranche_courante["ratio_count_above_upper_bound"] = (
                                    nb_above_seuil / self.elements_count
                                )
                            if nb_above_seuil > 0:
                                tranche_courante["mean_above_upper_bound"] = (
                                    sum_above_seuil / nb_above_seuil
                                )
                        else:
                            tranche_courante["count_above_upper_bound"] = 0
                            tranche_courante["sum_above_upper_bound"] = 0
                            tranche_courante["ratio_count_above_upper_bound"] = 0
                            tranche_courante["mean_above_upper_bound"] = 0

                        buckets.append(tranche_courante.copy())
                        #                         if debug:
                        #                             print(f"idrk={idrk} On change de frontière current_value={current_value} tranche_courante:{tranche_courante}")
                        # On passe au bucket suivant

                        tranche_courante = deepcopy(default_tranche)
                        tranche_courante["bucket_count"] = 1
                        tranche_courante["lower_bound"] = current_value
                        currbuck += 1
                        max_ff_bucket = current_value
                        sum_var_bucket = current_value
                        values = [current_value]
                else:
                    # We continue to iterate into the values in the same bucket
                    sum_var_bucket += current_value
                    values.append(current_value)
                    tranche_courante["upper_bound"] = current_value
                    tranche_courante["bucket_count"] += 1
                    if current_value > max_ff_bucket:
                        max_ff_bucket = current_value
            if secret_statistique_respecte:
                # On quitte la boucle seulement quand le secret statistique est respecté
                break

        buckets = sanitize_bucket(buckets)
        # On sauvegarde la distribution de ce bucket
        self.buckets = buckets

    def to_dict(self):
        """
        Exporte le résultat dans un dictionnaire Python
        """
        d = {
            "lower_bound": self.lower_bound,
            "upper_bound": self.upper_bound,
            "count": self.nbzero + self.nbnz
            if not self.mask_total_number_of_entity
            else SECRET_KEEPED,
            "count_zero": "whatever",
            "count_nonzero": "whatever",
            "buckets": self.buckets,
        }
        enforce_secret(d, self.nbzero, self.nbnz, self.minimal_bucket_size)
        return d


def get_fake_data(
    nb_echantillon_zero=1_000,
    nb_echantillon=10_000,
    var_name="var",
    set_some_var_to_zero=False,
    set_some_var_to_negative=True,
    exponent=1.5,
    divider=15,
):
    """
    Génération d'un faux jeu de données.
    """
    jeux = []

    idfoy = 0

    if set_some_var_to_negative:
        # On ajoute n où var est négatif
        for i in range(int(nb_echantillon * 0.1)):
            foyer = {
                "idfoy": idfoy,
                "revkire": 0,
                var_name: -1 * random.randint(0, i * 10),
            }
            jeux.append(foyer)
            idfoy += 1

    # Add n household to 0
    for i in range(nb_echantillon_zero):
        foyer = {
            "idfoy": idfoy,
            "revkire": 0,
            var_name: 0,
        }
        jeux.append(foyer)
        idfoy += 1

    for i in range(nb_echantillon):
        x = i * 100
        foyer = {
            "idfoy": idfoy,
            "revkire": x,
            # "var": random.randint(0,x ** 1.5 // (nb_echantillon // 15)) if random.random() > 0.5 else 0,
            var_name: x**exponent // (nb_echantillon // divider),
        }
        if set_some_var_to_zero and random.random() > 0.8:
            foyer[var_name] = 0
        jeux.append(foyer)
        idfoy += 1
    df = pd.DataFrame(jeux)
    return df


def pandas_to_vaex(df):
    return vaex.from_pandas(df)


def get_calib(vdf, variable, nb_bucket_var, minimal_bucket_size=12):
    """
    ::vdf:: Vaex DataFrame
    ::variable:: Column name to calibrate
    ::nb_bucket_var:: Number of bucket in wich to split the dataframe
    ::minimal_bucket_size:: Minimal number of sample in a bucket
    """
    une_tranche_rfr = get_primary_buckets(
        vdf, 1, minimal_bucket_size=minimal_bucket_size, debug=True
    )
    out = get_copulas(
        vdf,
        "revkire",
        variable,
        nb_bucket_var,
        une_tranche_rfr,
        minimal_bucket_size=minimal_bucket_size,
        debug=False,
    )

    return out["copules"][0]


def bucket_merge_with_above(calib_in, id_rm: int):
    """
    This method merge two bucket together.
    ::calib:: The buckets list
    ::id_rm:: The index of the bucket to merge with the bucket above
    """

    new_calib = copy.deepcopy(calib_in)
    # On supprime le bucket id_rm
    buck_removed = new_calib["buckets"].pop(id_rm)

    # On remplace les valeurs de celui qui est devenu le suivant
    new_calib["buckets"][id_rm]["lower_bound"] = buck_removed["lower_bound"]
    # new_calib["buckets"][id_rm]["upper_bound"] ne change pas
    new_calib["buckets"][id_rm]["bucket_count"] = (
        buck_removed["bucket_count"] + new_calib["buckets"][id_rm]["bucket_count"]
    )

    new_calib["buckets"][id_rm]["bucket_sum"] = (
        buck_removed["bucket_sum"] + new_calib["buckets"][id_rm]["bucket_sum"]
    )

    # new_calib["buckets"][id_rm]["count_above_upper_bound"] Ne change pas
    new_calib["buckets"][id_rm]["bucket_mean"] = (
        new_calib["buckets"][id_rm]["bucket_sum"]
        / new_calib["buckets"][id_rm]["bucket_count"]
    )
    new_calib["buckets"][id_rm]["bucket_stdev"] = 0

    # On verifie qu'on ne perd personne en cours de route
    tot_av = 0
    tot_ap = 0
    for i in range(len(calib_in["buckets"])):
        tot_av += calib_in["buckets"][i]["bucket_count"]
    for j in range(len(new_calib["buckets"])):
        tot_av
        tot_ap += new_calib["buckets"][j]["bucket_count"]

    tc.assertEqual(tot_av, tot_ap)

    return new_calib


def reduce_bucket_number(calib, max_gap: int):
    """
    This method scans a bucket list and merges all buckets where
    ::calib:: The buckets list
    ::max_gap:: The ratio below which the bucket will be merged
    """
    calib_new = {}
    calib_new = copy.deepcopy(calib)
    last = False

    # On décide de recommencer à parcourir la nouvelle liste dès qu'on a fusionné un bucket
    while last is False:
        buckets = calib_new["buckets"]
        for idx, bucket in enumerate(buckets):
            # On s'arrete 2 buckets avant la fin
            if idx + 2 == len(buckets):
                last = True
                break
            # Bucket vide
            elif buckets[idx]["bucket_mean"] == 0.0:
                continue
            # Sinon:
            else:
                ecart = buckets[idx + 1]["bucket_mean"] - bucket["bucket_mean"]
                moyenne = (bucket["bucket_mean"] + buckets[idx + 1]["bucket_mean"]) / 2
                if (ecart < max_gap * moyenne) and (
                    buckets[idx + 1]["bucket_mean"] != 0
                ):
                    # print("to remove", idx)
                    calib_new = bucket_merge_with_above(calib_new, idx)
                    break
    print(
        "On a fusionné les buckets, passant de ",
        len(calib["buckets"]),
        " à ",
        len(calib_new["buckets"]),
        "buckets \n",
    )

    return calib_new


def get_copules_revkire(
    vdf, nb_bucket, variable, nb_bucket_var, minimal_bucket_size=12, debug=True
):
    tranche_rfr = get_primary_buckets(
        vdf,
        nb_bucket,
        minimal_bucket_size=minimal_bucket_size,
        debug=debug,
    )
    copules = get_copulas(
        vdf,
        "revkire",
        variable,
        nb_bucket_var,
        tranche_rfr,
        debug=debug,
        minimal_bucket_size=minimal_bucket_size,
    )
    return copules


def compute_pop_copules(copules):
    nb_pop = 0
    for c in copules["copules"]:
        if isinstance(c["count"], int):
            nb_pop += c["count"]
    return nb_pop


def anonimyze_value(val: Union[float, int], min_len: int = 0):
    """
    Make value secret by rounding it:
        - 1 to 9 became 10
        - 125.55 became 1 000
    Handle also negative value.
    Don't change if length of value smaller than min_len.
    Arg:
        val: Value to make secret
        min_len: Minimal length of value to make change.
    Return:
        The secret value
    """
    val_str = str(abs(int(val)))
    # No change if already filled with 0
    zeros = "".join(["0" for i in range(len(val_str) - 1)])
    if val_str[-(len(val_str) - 1) :] == zeros:
        return val
    else:
        try:
            # Don't change if smaller than min_len
            if len(val_str) <= min_len:
                return val
            if val < 0:
                return -(10 ** (len(val_str)))
            elif val == 0.0:
                return 0
            else:
                return 10 ** (len(str(int(val))))
        except Exception as e:
            print(val)
            raise e


def anonimyze_lower_and_upper_bound(content, min_len: int = 4):
    """
    Make upper bound secret, and lower bound as well.
    Change the first bucket lower bound and the last bucket upper bound

    Handle distribution
    {'lower_bound': 0.0,
     'upper_bound': 12124000.0,
     'buckets': [
         {'lower_bound': 0.0,
          'upper_bound': 0.0,
         }]
    }

    Handle distribution, without main infos
    [
         {'lower_bound': 0.0,
          'upper_bound': 0.0,
         }
    ]

    Handle copulas
    {"controle": [], "copules": [{"lower_bound": 0.0, "upper_bound": 8.0, "count": {"zero": 2758951, "nonzero": 8106}, "buckets": [{"lower_bound"

    """
    json_content = content
    if content == [] or isinstance(content, str):
        return

    def _anonimyze_dict(content: dict, key: str, min_len: int = 0):
        val = content.get(key)
        if val:
            new_val = anonimyze_value(val, min_len)
            # Prevent change on lower_bound to be above upper_bound
            if (
                key == "lower_bound"
                and content.get("upper_bound") is not None
                and new_val > content.get("upper_bound")
            ):
                return
            else:
                content[key] = new_val

    if isinstance(content, dict) and content.get("copules"):
        content = content.get("copules")

    if isinstance(content, dict) and content.get("upper_bound"):
        _anonimyze_dict(content, "lower_bound", min_len)
        _anonimyze_dict(content, "upper_bound")
        if content.get("buckets"):
            content = content.get("buckets")
    # Change Lower Bound
    if isinstance(content, list) and content[0].get("lower_bound"):
        _anonimyze_dict(content[0], "lower_bound", min_len)

    # Change Lower Bound
    if isinstance(content, list) and content[-1].get("upper_bound"):
        _anonimyze_dict(content[-1], "upper_bound")

    # Change Copulas Bounds
    if content[-1].get("buckets"):
        for buck in content:
            if buck["buckets"] == [] or isinstance(buck["buckets"], str):
                continue
            # Lower bound
            _anonimyze_dict(buck["buckets"][0], "lower_bound", min_len)
            # Upper bound
            _anonimyze_dict(buck["buckets"][-1], "upper_bound", min_len=0)

    else:
        # In Calib
        # Upper bound
        val = content[-1].get("upper_bound")
        if val:
            if isinstance(val, str):
                content[-1]["upper_bound"] = anonimyze_value(val)
        # Lower bound
        val = content[0].get("lower_bound")
        if val:
            if isinstance(val, str):
                new_val = anonimyze_value(val, min_len)
                content[0]["lower_bound"] = (
                    new_val if new_val < content[0]["upper_bound"] else val
                )
    return json_content


def copules_to_df(copules):
    copules_flat = []
    # nb_pop = compute_pop_copules(copules)
    # On vérifie que l'on est au bon niveau
    if not isinstance(copules, list):
        if copules.get("copules"):
            copules = copules["copules"]
    tc.assertIsNotNone(copules[0].get("buckets"))
    for cop in copules:
        for bucket in cop["buckets"]:
            if cop.get("nb_foyer"):
                """
                Gestion de l'ancien formats:
                {'lower_bound': 36541012.0,
                 'upper_bound': 1000000000000000,
                 'nb_foyer': {'zero': 11, 'nonzero': 27},
                'buckets': [{'seuil_var_inf': 0,
                   'seuil_var_supp': 0,
                   'nombre_ff_tranche': 11,
                   'sum_tranche_var': 0,
                   'mean_tranche_var': 0,
                   'nb_above_seuil': 27,
                   'sum_var_above_seuil': 42868098.0,
                   'ratio_nb_above_seuil': 0.7105263157894737,
                   'mean_var_above_seuil': 1587707.3333333333},
                """
                un_copule = {
                    "lower_bound": cop["lower_bound"],
                    "upper_bound": cop["upper_bound"],
                    "count_zero": cop["nb_foyer"]["zero"],
                    "count_nonzero": cop["nb_foyer"]["nonzero"],
                    "bucket_lower_bound": bucket["seuil_var_inf"],
                    "bucket_upper_bound": bucket["seuil_var_supp"],
                    "bucket_count": bucket["nombre_ff_tranche"],
                    "bucket_sum": bucket["sum_tranche_var"],
                    "bucket_mean": bucket["mean_tranche_var"],
                    "bucket_count_above_upper_bound": bucket["nb_above_seuil"],
                    "bucket_sum_above_upper_bound": bucket["sum_var_above_seuil"],
                    "bucket_ratio_count_above_upper_bound": bucket[
                        "ratio_nb_above_seuil"
                    ],
                    "bucket_mean_above_upper_bound": bucket["mean_var_above_seuil"],
                }

            else:
                un_copule = {
                    "lower_bound": cop["lower_bound"],
                    "upper_bound": cop["upper_bound"],
                    "count_zero": cop["count_zero"],
                    "count_nonzero": cop["count_nonzero"],
                    "bucket_lower_bound": bucket["lower_bound"],
                    "bucket_upper_bound": bucket["upper_bound"],
                    "bucket_count": bucket["bucket_count"],
                    "bucket_sum": bucket["bucket_sum"],
                    "bucket_mean": bucket["bucket_mean"],
                    "bucket_count_above_upper_bound": bucket["count_above_upper_bound"],
                    "bucket_sum_above_upper_bound": bucket["sum_above_upper_bound"],
                    "bucket_ratio_count_above_upper_bound": bucket[
                        "ratio_count_above_upper_bound"
                    ],
                    "bucket_mean_above_upper_bound": bucket["mean_above_upper_bound"],
                }
            copules_flat.append(un_copule)
    return pd.DataFrame(copules_flat)


def calib_to_df(calib):
    return copules_to_df([calib])


def copulas_to_array(copulas, key: str = "bucket_mean"):
    tc.assertIsNotNone(copulas[0].get("buckets"))
    copulas_2d = []
    col_lower_bound = []
    max_row_lower_bound = []
    for cop in copulas:
        line = []
        row_lower_bound = []
        col_lower_bound.append(cop["lower_bound"])
        if not isinstance(cop["buckets"], (list, CommentedSeq)):
            print(f"WARNING : Empty bucket : {cop['buckets']}!")
            line.append([])
        else:
            for bucket in cop["buckets"]:
                line.append(bucket[key])
                row_lower_bound.append(bucket["lower_bound"])
        if len(row_lower_bound) > len(max_row_lower_bound):
            max_row_lower_bound = row_lower_bound
        copulas_2d.append(line)
    copulas_dict = {
        "array": copulas_2d,
        "col_lower_bound": col_lower_bound,
        "row_lower_bound": max_row_lower_bound,
    }
    return copulas_dict


def get_ecart_frontiere(frontieres, minimal_bucket_size=12):
    prec = 0
    ecart = []
    for f in frontieres:
        e = f - prec
        if e < minimal_bucket_size:
            return False
        ecart.append(e)
        prec = f
    return ecart
