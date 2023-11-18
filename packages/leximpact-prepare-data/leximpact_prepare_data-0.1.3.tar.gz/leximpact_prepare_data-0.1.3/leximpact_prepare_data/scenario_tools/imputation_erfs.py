from openfisca_survey_manager.survey_collections import SurveyCollection
from leximpact_common_python_libraries.config import Configuration
import pandas as pd
import numpy as np
import json
from openfisca_survey_manager.input_dataframe_generator import set_table_in_survey
from openfisca_france_data.erfs_fpr.input_data_builder.step_01_preprocessing import (
    build_table_by_name,
)


def add_cases_ir_from_erfs(period):
    erfs_fpr_survey_collection = SurveyCollection.load(collection="erfs_fpr")
    table_by_name = build_table_by_name(2019, erfs_fpr_survey_collection)
    leximpact_survey_collection = SurveyCollection.load(collection="leximpact")
    idents = (
        SurveyCollection.load(collection="openfisca_erfs_fpr")
        .get_survey("openfisca_erfs_fpr_2019")
        .get_values(table="individu_2019", ignorecase=True)
    )
    ident_foy_with_pac = idents.loc[idents["quifoy"] == 2].idfoy.unique()
    idents = idents.loc[idents.quifoy == 0][
        ["idmen_original", "idfoy", "date_naissance", "statut_marital"]
    ]
    nivviem = erfs_fpr_survey_collection.get_survey("erfs_fpr_2019").get_values(
        table=table_by_name["fpr_menage"], ignorecase=True
    )[["ident", "nivviem", "wprm"]]
    nivviem.columns = ["idmen_original", "nivviem", "wprm"]
    nivviem = pd.merge(nivviem, idents, on="idmen_original")
    leximpact_foyers = leximpact_survey_collection.get_survey(
        "leximpact_2019"
    ).get_values(table="foyer_fiscal_2019", ignorecase=True)
    leximpact_foyers["idfoy"] = leximpact_foyers.index
    leximpact_foyers = pd.merge(leximpact_foyers, nivviem, on="idfoy")
    leximpact_foyers["date_naissance"] = (
        np.floor(leximpact_foyers.date_naissance.dt.year / 10) * 10
    )
    leximpact_foyers.sort_values("nivviem", ascending=True, inplace=True)
    leximpact_foyers["quantile"] = np.ceil(
        10 * leximpact_foyers.wprm.cumsum() / leximpact_foyers.wprm.sum()
    )
    config = Configuration(project_folder="leximpact-prepare-data")
    aggregates_path = config.get("AGREGATS_PATH")

    with open(f"{aggregates_path}ERFS/2019/demi_part_invalidite.json") as f:
        test = json.load(f)

    index_invalidite = []
    for quant in range(1, 11):
        sub_target = test["data"][str(quant)]
        for sub_sub_target in sub_target:
            temp = leximpact_foyers.loc[leximpact_foyers["quantile"] == quant].loc[
                leximpact_foyers["date_naissance"] == sub_sub_target["decennie_naispr"]
            ]
            temp["rand"] = np.random.random(len(temp))
            temp.sort_values("rand", ascending=True, inplace=True)
            temp["cumsum"] = temp.wprm.cumsum()
            index_invalidite += temp.loc[
                temp["cumsum"] <= sub_sub_target["somme_wprm"]
            ].index.to_list()

    with open(f"{aggregates_path}ERFS/2019/demi_part_parent_isole.json") as f:
        test = json.load(f)

    index_parent_isole = []
    parents_isoles = leximpact_foyers.iloc[ident_foy_with_pac].loc[
        leximpact_foyers["statut_marital"] == 2
    ]
    for quant in range(1, 11):
        sub_target = test["data"][str(quant)]
        for sub_sub_target in sub_target:
            temp = parents_isoles.loc[parents_isoles["quantile"] == quant].loc[
                parents_isoles["date_naissance"] == sub_sub_target["decennie_naispr"]
            ]
            temp["rand"] = np.random.random(len(temp))
            temp.sort_values("rand", ascending=True, inplace=True)
            temp["cumsum"] = temp.wprm.cumsum()
            index_parent_isole += temp.loc[
                temp["cumsum"] <= sub_sub_target["somme_wprm"]
            ].index.to_list()

    leximpact_foyers = leximpact_survey_collection.get_survey(
        f"leximpact_{period}"
    ).get_values(table=f"foyer_fiscal_{period}", ignorecase=True)
    leximpact_foyers["caseT"] = False
    leximpact_foyers.loc[index_parent_isole, "caseT"] = True
    leximpact_foyers["caseP"] = False
    leximpact_foyers.loc[index_invalidite, "caseP"] = True

    set_table_in_survey(
        leximpact_foyers,
        entity="foyer_fiscal",
        period=period,
        collection="leximpact",
        survey_name=f"leximpact_{period}",
    )

    leximpact_individus = leximpact_survey_collection.get_survey(
        f"leximpact_{period}"
    ).get_values(table=f"individu_{period}", ignorecase=True)

    leximpact_individus.drop("revenus_minimum_menage", axis=1, inplace=True)

    leximpact_individus["revenus"] = (
        leximpact_individus["salaire_de_base"]
        + leximpact_individus["rpns_imposables"]
        + leximpact_individus["traitement_indiciaire_brut"]
        + leximpact_individus["retraite_brute"]
        + leximpact_individus["chomage_brut"]
        + (1e9 * (leximpact_individus["quimen"] == 2))
    )

    temp = pd.DataFrame()
    temp["revenus_minimum_menage"] = leximpact_individus.groupby(
        "idmen", group_keys=False
    ).revenus.apply(lambda x: min(x))
    temp.index.name = None
    temp["idmen"] = temp.index
    leximpact_individus = pd.merge(leximpact_individus, temp, on="idmen", how="inner")
    leximpact_individus["revenus_minimum_menage"] = (
        leximpact_individus["revenus_minimum_menage"] == leximpact_individus["revenus"]
    )
    leximpact_individus.drop("revenus", axis=1, inplace=True)

    # ajout d'une variable aléatoire pour tirer du non recours
    np.random.seed(25)
    leximpact_individus["random_var"] = np.random.random(
        size=len(leximpact_individus.index)
    )

    set_table_in_survey(
        leximpact_individus,
        entity="individu",
        period=period,
        collection="leximpact",
        survey_name=f"leximpact_{period}",
    )
