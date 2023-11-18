import numpy as np
import pandas as pd
from openfisca_survey_manager.input_dataframe_generator import set_table_in_survey
from openfisca_survey_manager.survey_collections import SurveyCollection

# from ..leximpact_survey_scenario import future_monte_carlo_variables


def duplicate_rows(year, collection, weight_max):
    survey_collection = SurveyCollection.load(collection="openfisca_erfs_fpr")
    survey = survey_collection.get_survey(f"openfisca_erfs_fpr_{year}")
    tables = set(survey.tables.keys())
    for entity in ["individu", "menage"]:
        assert f"{entity}_{year}" in tables

    menages = survey.get_values(table=f"menage_{year}", ignorecase=True)
    individus = survey.get_values(table=f"individu_{year}", ignorecase=True)

    old_wprm = menages.wprm.sum()

    menages.rename(columns={"idmen": "old_idmen"}, inplace=True)
    menages["nb_duplication"] = np.floor(menages.wprm / weight_max)
    menages.loc[menages["nb_duplication"] == 0, "nb_duplication"] == 1
    menages_dupl = menages[["old_idmen", "nb_duplication"]]
    menages = menages.loc[np.repeat(menages.index.values, menages.nb_duplication)]
    menages.rename(columns={"wprm": "old_wprm"}, inplace=True)
    menages["wprm"] = round(menages.old_wprm / menages.nb_duplication, 2)
    menages.drop(columns=["nb_duplication"], inplace=True)
    menages.reset_index(drop=True, inplace=True)

    menages["idmen"] = range(len(menages))
    individus.rename(columns={"idmen": "old_idmen"}, inplace=True)
    nb_pers = pd.DataFrame(individus.groupby("old_idmen").size(), columns=["mensize"])
    menages_temp = pd.merge(nb_pers, menages[["old_idmen", "idmen"]], on="old_idmen")
    menages_temp = menages_temp.loc[
        np.repeat(menages_temp.index.values, menages_temp.mensize)
    ]
    individus["id"] = individus.groupby("old_idmen").cumcount()
    individus = pd.merge(menages_dupl, individus, on="old_idmen")
    individus = individus.loc[
        np.repeat(individus.index.values, individus.nb_duplication)
    ]

    menages_temp["id"] = menages_temp.groupby("idmen").cumcount()
    menages_temp.sort_values(["old_idmen", "id"], inplace=True)
    menages_temp.reset_index(drop=True, inplace=True)
    individus.sort_values(["old_idmen", "id"], inplace=True)
    individus.reset_index(drop=True, inplace=True)
    individus = pd.concat([individus, menages_temp["idmen"]], axis=1)

    individus.drop(columns=["nb_duplication", "id"], inplace=True)
    individus.reset_index(drop=True, inplace=True)
    individus.rename(columns={"idfoy": "old_idfoy"}, inplace=True)
    id_ff = individus[["old_idfoy", "idmen"]].drop_duplicates()
    id_ff["idfoy"] = range(len(id_ff))
    individus = pd.merge(individus, id_ff, how="inner", on=["old_idfoy", "idmen"])
    individus["idfam"] = individus.idfoy.copy()
    individus["old_idfam"] = individus.old_idfoy.copy()

    new_wprm = menages.wprm.sum()
    evol = 100 * (new_wprm - old_wprm) / old_wprm

    print(
        f"Poids avant duplication : {old_wprm}, poids après duplication : {new_wprm}, soit {evol} % "
    )

    # Formats ids
    unique_idmen = individus[["idmen"]].drop_duplicates()
    assert len(unique_idmen) == len(
        menages
    ), f"Number of idmen should be the same individus ({len(unique_idmen)}) and menages ({len(menages)}) table"

    # Enters the individual table into the openfisca_erfs_fpr collection
    individus.sort_values(by=["idmen", "idfoy", "idfam", "quimen"], inplace=True)
    individus.reset_index(drop=True, inplace=True)

    print(f"collection : {collection}")

    set_table_in_survey(
        individus,
        entity="individu",
        period=year,
        collection="openfisca_erfs_fpr_duplicated",
        survey_name="openfisca_erfs_fpr_duplicated_2019",
    )

    menages.sort_values(by=["idmen"], inplace=True)
    menages.reset_index(drop=True, inplace=True)

    set_table_in_survey(
        menages,
        entity="menage",
        period=year,
        collection="openfisca_erfs_fpr_duplicated",
        survey_name="openfisca_erfs_fpr_duplicated_2019",
    )


# def optimization_duplicates_rows(year, collection = "leximpact"):
#     survey_collection = SurveyCollection.load(collection = collection)
#     survey = survey_collection.get_survey(f"{collection}_{year}")
#     tables = set(survey.tables.keys())
#     for entity in ["foyer_fiscal", "individu", "menage"]:
#         assert f"{entity}_{year}" in tables

#     menages = survey.get_values(table = f"menage_{year}", ignorecase= True)
#     individus = survey.get_values(table = f"individu_{year}", ignorecase= True)
#     foyers_fiscaux = survey.get_values(table = f"foyer_fiscal_{year}", ignorecase= True)

#     if "old_idfoy" in foyers_fiscaux.columns(): # si cette variable existe c'est qu'il y a eu un duplicates et donc qu'il y a potentiellement une optimisation possible

#         foyers_fiscaux['tot'] = 0
#         for var in future_monte_carlo_variables:
#             if var in foyers_fiscaux.columns:
#                 foyers_fiscaux['tot'] += foyers_fiscaux[var]

#         duplicates = foyers_fiscaux.loc[foyers_fiscaux.tot == 0]
#         duplicates = duplicates.groupby('old_idfoy').agg({'wprm':'sum'})
#         foyers_fiscaux = foyers_fiscaux.drop(['idfoy', 'wprm']).drop_duplicates()
#         assert len(duplicates.index) == len(foyers_fiscaux.index), "Il y a un problème dans l'optimisation de la duplication"

#         foyers_fiscaux = pd.merge(foyers_fiscaux, duplicates, on = 'old_idfoy')
