import unittest
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from leximpact_aggregates.aggregate import AggregateManager
from leximpact_common_python_libraries.config import Configuration
from leximpact_survey_scenario.scenario_tools.helpers_survey_scenario import (
    distrib_to_quantiles,
    generate_title,
    get_quantiles_casd,
)

config = Configuration(project_folder="leximpact-prepare-data")
tc = unittest.TestCase()

aggregates_path = config.get("AGREGATS_PATH")

annee_erfs = 2019
annee_pote = 2019


def agg_lib():
    aggm_c = AggregateManager(aggregates_path=aggregates_path)
    return aggm_c


def get_copules(year, new_var, nb_copules, copules_var=None):
    data_structure = "copulas_" + nb_copules
    agg = agg_lib()
    agg.load_aggregate(
        "POTE",
        new_var,
        year=str(year),
        data_structure=data_structure,
        copules_var=copules_var,
    )
    return agg.aggregate.data[-1].values


def compare_distributions(
    df_erfs,
    df_pote,
    var_name,
    annee_erfs,
    annee_pote,
    title_suffix,
    log=None,
    df_cal=[],
):
    annee_erfs = str(annee_erfs)
    annee_pote = str(annee_pote)

    # Pour traiter le cas des buckets vides, on remplace les NaN par zéro
    df_pote["mean"] = df_pote["mean"].fillna(0)
    df_erfs["mean"] = df_erfs["mean"].fillna(0)
    if len(df_cal) != 0:
        df_cal["mean"] = df_cal["mean"].fillna(0)

    # Création d'une figure
    fig = plt.figure(figsize=(18, 8), facecolor="white", clear=True)
    ax = sns.barplot(data=df_pote, y="sum", x=df_pote.index, alpha=0.5, color="blue")
    ax = sns.barplot(data=df_erfs, y="sum", x=df_erfs.index, alpha=0.5, color="red")
    outname = (
        var_name
        + "_ERFS_"
        + str(annee_erfs)
        + "_POTE_"
        + str(annee_pote)
        + "_"
        + title_suffix
    )

    # S'il y a une calibration
    if len(df_cal) != 0:
        ax = sns.barplot(data=df_cal, y="sum", x=df_cal.index, alpha=0.5, color="green")
        title = generate_title(var_name, annee_erfs, annee_pote, title_suffix, cal=True)
        outname = "Distributions_de_" + outname
        df_base = df_cal.copy()

    else:
        title = generate_title(
            var_name, annee_erfs, annee_pote, title_suffix, cal=False
        )
        outname = "Calibration_de_" + outname
        df_base = df_erfs.copy()

    # Si échelle logarithmique
    if log:
        _ = ax.set_yscale("log")
        _ = ax.set_title(
            (title + "\n Echelle de population logarithmique"), fontsize=18
        )
    else:
        _ = ax.set_title(title, fontsize=18)

    # Axis Setup
    xticks = [i for i in range(len(df_pote["middle"]))]
    xlabels = [f"{str(round(j / (10 ** 3), 2))} k€" for j in df_pote["mean"]]
    _ = ax.set_xticks(xticks)
    _ = ax.set_xticklabels(xlabels, rotation=75)
    _ = ax.set_xlabel(
        " ' " + var_name + " ' " + " moyen pour chaque quantile (POTE)", fontsize=16
    )
    _ = ax.set_ylabel("Somme de " + var_name + " dans chaque quantile", fontsize=16)

    # Plotting the sum on top of the bars
    # ax.margins(y=0.1)
    # for bars in ax.containers:
    #    ax.bar_label(bars, fmt='%.1f')

    # Saving the figure
    figpath = config.get("PLOTS")
    plt.savefig((figpath + outname), bbox_inches="tight")

    # On calcule l'erreur comme la moyenne des erreurs de chaque bucket
    error_df = 100 * pd.Series(abs(df_pote["sum"] - df_base["sum"]) / df_pote["sum"])
    # Pour le premier bucket, les sommes sont à zéro donc on mesure l'erreur en Nb de foyers
    error_df[0] = (
        100 * abs(df_pote["nb_ff"][0] - df_base["nb_ff"][0]) / df_pote["nb_ff"][0]
    )
    # On exclut les quantiles nuls du calcul d'erreur
    final_error = (error_df.sum()) / (len(df_base))
    print("Erreur moyenne des buckets de ", var_name, " : ", final_error, " %")
    print("Erreur min : ", min(error_df), "erreur max: ", max(error_df))

    return fig, error_df, final_error


def pote_comparison(base_ff, variable, title_suffix=None, log=None, base_ff_cal=None):
    # Obtention des quantiles de POTE
    quantiles = get_quantiles_casd(variable)
    assert quantiles is not None
    print(base_ff.keys())
    # On garde les notations utilisées pour le calcul
    base_ff["wprm"] = base_ff["weight_foyers"]
    base_ff["idfoy"] = base_ff["foyer_fiscal_id"]

    # Distribution de la base sur les quantiles de POTE
    Distrib_BASE, Distrib_POTE, quantiles = distrib_to_quantiles(
        base_ff, variable, quantiles
    )
    poids_avant = base_ff["weight_foyers"].copy()
    print("Somme des poids avant calibration", poids_avant.sum())

    if base_ff_cal is not None:
        print("Somme des poids après calibration", base_ff_cal["weight_foyers"].sum())
        # On garde les notations utilisées pour le calcul
        base_ff_cal["wprm"] = base_ff_cal["weight_foyers"]
        base_ff_cal["idfoy"] = base_ff_cal["foyer_fiscal_id"]

        # Distribution de la base sur les quantiles de POTE
        Distrib_BASE_CAL, Distrib_POTE_2, quantiles = distrib_to_quantiles(
            base_ff_cal, variable, quantiles
        )

        # Comparaison des distributions
        fig, error_df, final_error = compare_distributions(
            Distrib_BASE.df,
            Distrib_POTE.df,
            variable,
            annee_erfs,
            annee_pote,
            title_suffix,
            log,
            df_cal=Distrib_BASE_CAL.df,
        )

        print(
            "Total de ",
            variable,
            "avant :",
            (base_ff[variable] * poids_avant).sum(),
            "et après calibration :",
            (base_ff_cal["weight_foyers"] * base_ff_cal[variable]).sum(),
        )
    else:
        # Comparaison des distributions
        fig, error_df, final_error = compare_distributions(
            Distrib_BASE.df,
            Distrib_POTE.df,
            variable,
            annee_erfs,
            annee_pote,
            title_suffix,
            log,
            df_cal=[],
        )

    return fig, error_df, final_error
