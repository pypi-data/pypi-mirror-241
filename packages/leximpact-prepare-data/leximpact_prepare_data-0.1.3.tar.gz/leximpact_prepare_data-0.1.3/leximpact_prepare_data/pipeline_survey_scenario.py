import logging
import unittest
from multiprocessing import Process, Queue
from typing import Any, Optional

import numpy as np
import pandas as pd

from openfisca_core.taxbenefitsystems import TaxBenefitSystem

from openfisca_survey_manager.input_dataframe_generator import set_table_in_survey

from leximpact_prepare_data.scenario_tools.helpers_survey_scenario import get_copules

from leximpact_prepare_data.scenario_tools.monte_carlo_computer import apply_Monte_Carlo
from leximpact_survey_scenario.leximpact_survey_scenario import (
    LeximpactErfsSurveyScenario,
)

from openfisca_france_data.erfs_fpr.input_data_builder import build
from leximpact_prepare_data.pipeline_tax_and_benefit_system import pipeline_tbs

tc = unittest.TestCase()
pd.set_option("display.max_columns", None)
log = logging.getLogger(__name__)

# Liste des variables qui sont injectées par Monte-Carlo et ajoutée en input variable du survey_scenario
## sous liste en fonction de la variable primaire par laquelle on impute
variables_by_revenu_individuels_100 = [
    "revenu_categoriel_foncier",
    "rente_viagere_titre_onereux_net",
    "revenus_capitaux_prelevement_bareme",
    "revenus_capitaux_prelevement_forfaitaire_unique_ir",
    "revenus_capitaux_prelevement_liberatoire",
]
variables_by_revenus_individuels_20 = [
    "assiette_csg_plus_values",
]

variables_by_revkire_par_part = ["reductions", "credits_impot", "charges_deduc"]
future_monte_carlo_variables = (
    variables_by_revenu_individuels_100
    + variables_by_revenus_individuels_20
    + variables_by_revkire_par_part
)


class PipelineErfsSurveyScenario(LeximpactErfsSurveyScenario):
    """Survey scenario spécialisé pour l'ERFS-FPR utilisée par Leximpact."""

    def __init__(
        self,
        annee_donnees: int = 2019,
        period: int = 2023,
        rebuild_input_data: bool = False,
        # rebuild_input_data est un paramètre hérité de survey_manager. Si True relance le build de openfisca_france_data
        init_from_data: bool = True,
        baseline_tax_benefit_system: Optional[TaxBenefitSystem] = pipeline_tbs,
        data: Any = None,
        collection: str = "openfisca_erfs_fpr",
        survey_name: str = None,
    ):
        """Crée un `LeximpactErfsSurveyScenario`.

        :param annee_donnees                L'année des données utilisées en input.
        :param rebuild_input_data:          Si l'on doit formatter les données (raw) ou pas.
        :param init_from_data:              Si on veut suspendre l'initialisation automatique par les données
        :param tax_benefit_system:          Le `TaxBenefitSystem` déjà réformé.
        :param baseline_tax_benefit_system: Le `TaxBenefitSystem` au droit courant.
        :param data:                        Les données de l'enquête.
        :param reform:                      Reform OpenFisca.
        :param collection:                  Collection à lire.
        :param survey_name:                 Nom de l'enquête.
        """
        self.used_as_input_variables = list(
            set(
                self.used_as_input_variables
                + ["prest_precarite_hand", "revenus_minimum_menage"]
            )
        )

        super().__init__(
            annee_donnees=annee_donnees,
            period=period,
            rebuild_input_data=rebuild_input_data,
            init_from_data=init_from_data,
            baseline_tax_benefit_system=baseline_tax_benefit_system,
            data=data,
            collection=collection,
            survey_name=survey_name,
        )
        self.used_as_input_variables = list(
            set(
                self.used_as_input_variables
                + ["prest_precarite_hand", "revenus_minimum_menage"]
            )
        )

    def build_input_data(self, year: int) -> None:
        build(year=year)

    def build_imputation(self, year):
        self.injector(year, "revenus_individuels", variables_by_revenu_individuels_100)
        self.injector(
            year,
            "revenus_individuels",
            variables_by_revenus_individuels_20,
            nb_copules="20",
        )
        if self.collection == "openfisca_erfs_fpr":
            variables_by_revkire_par_part.remove("charges_deduc")
        self.injector(year, "revkire_par_part", variables_by_revkire_par_part)

        t_b_variables = list(
            self.tax_benefit_systems["baseline"].get_variables().keys()
        )
        for y in range(int(year) - 3, int(year) + 1):
            variables_to_keep = self.used_as_input_variables
            for t_b_variable in t_b_variables:
                if t_b_variable not in variables_to_keep:
                    self.simulations["baseline"].delete_arrays(t_b_variable, period=y)

    def monte_carlo_computer(
        self, year, reference_var, new_var, nb_copules, by_quantile=True
    ):
        # Charger les copules
        copules = get_copules(year, new_var, nb_copules, reference_var)

        # On travaille avec une unique entité pour reference_var et new_var (pour le moment: les foyers)
        ref_entity = (
            self.tax_benefit_systems["baseline"].get_variable(reference_var).entity.key
        )
        var_entity = (
            self.tax_benefit_systems["baseline"].get_variable(new_var).entity.key
        )

        if var_entity == ref_entity == "foyer_fiscal":
            data_frame_by_entity = self.simulations[
                "baseline"
            ].create_data_frame_by_entity(
                variables=[reference_var, new_var, "weight_foyers"], period=year
            )
            df = data_frame_by_entity["foyer_fiscal"]
        else:
            raise Exception(
                "Attention, (pour l'instant) on ne peut calculer les copules que d'une variable en foyers vers une variable en foyers"
            )
        if by_quantile:
            nb_quantile = len(copules)
            df_zero = df.loc[df[reference_var] == 0].copy()
            df_zero["quantiles"] = 1
            df_nonzero = (
                df.loc[df[reference_var] != 0]
                .sort_values(reference_var, ascending=True)
                .copy()
            )
            df_nonzero["quantiles"] = (
                np.minimum(
                    np.ceil(
                        (nb_quantile - 1)
                        * df_nonzero.weight_foyers.cumsum()
                        / df_nonzero.weight_foyers.sum()
                    ),
                    (nb_quantile - 1),
                )
                + 1
            )

            df = pd.concat([df_zero, df_nonzero])
            df = df.sort_index()
        # On travaille directement avec une base en foyers
        df, errors = apply_Monte_Carlo(
            df,
            copules,
            bucket_level_col_name=reference_var,
            by_quantile=by_quantile,
            out_col=new_var,
            weight_var="weight_foyers",
            nb_tirage=1,  # 20
            seed=25,
            use_force_mean_with_factor=False,
            debug=False,
        )

        # On vérifie qu'on a toujours le même total de poids dans la base et dans la simulation (ie. pas de distortion)
        tc.assertEqual(
            self.simulations["baseline"].calculate("weight_foyers", period=year).sum(),
            df["weight_foyers"].sum(),
        )
        return df[new_var]

    def monte_carlo_injector(
        self, reference_var, var, year, res_queue: Queue, nb_copules
    ):
        """
        Task for parallel processing
        Arg:
            scenario: scenario instance
            var: variable to inject
        return an array with the data
        """
        print(f"Injection de {var}")
        # Calcul de la nouvelle variable par Monte-Carlo à partir des copules de POTE
        result_array = self.monte_carlo_computer(year, reference_var, var, nb_copules)
        res_queue.put({var: result_array})

    def injector(self, year, reference_var, variables_to_inject, nb_copules="100"):
        """
        Fonction d'injection de variable par l'algorithme de Monte-Carlo

        :year:              Année d'injection (année de la base ET des copules)
        :reference_var:     Variable de référence pour les copules (par exemple, RFR)
        :new_var:           Variables à ajouter dans la base (elles doivent toutes avoir la même `reference_var`)
        """
        # TODO : Permettre l'injection de variables individus SI un jour on utilise d'autres bases que POTE
        # "L'injection se fait avec des copules de POTE, donc uniquement d'une variable en foyers à une variable en foyers"

        processes = []
        results = []
        q = Queue()
        # On génère la liste des appels à lancer
        for v in variables_to_inject:
            p = Process(
                target=self.monte_carlo_injector,
                args=(reference_var, v, year, q, nb_copules),
            )
            processes.append(p)
        # On lance les appels
        [p.start() for p in processes]
        # On récupère les résultats
        [results.append(q.get()) for p in processes]
        # On traite les résultats
        for res in results:
            for variable, array in res.items():
                self.simulations["baseline"].delete_arrays(variable, year)
                self.simulations["baseline"].set_input(variable, year, array)

    def save_current_survey(
        self,
        variables,
        collection: str = "openfisca_erfs_fpr",
        survey_name: str = None,
        period: str = None,
    ):
        """
        Récupére tous les dataframes de toutes les entités et les sauve dans le survey scenario
        """
        if survey_name is None:
            survey_name = f"{collection}_{self.annee_donnees}"

        if variables is None:
            variables = self.used_as_input_variables
        if period is None:
            for year in range(self.annee_donnees, int(self.period) + 1):
                # merge=True permet d'obtenir les variables clef pour pouvoir faire des merge ensuite avec les données.
                data_frame_by_entity = self.simulations[
                    "baseline"
                ].create_data_frame_by_entity(
                    variables=variables, period=year, index=True
                )

                for entity, input_dataframe in data_frame_by_entity.items():
                    assert type(input_dataframe) == pd.DataFrame
                    print(
                        f"set_table_in_survey of {entity} for {year} in {collection}.{survey_name}"
                    )

                    # TODO Ajouter idfoy_original de ErfsFprSurveyScenario ? Serait l'identifiant de l'enquête ERFS-FPR.
                    if entity == "foyer_fiscal":
                        # ISSUE idfoy d'individus ne correspond pas à la cardinalité d'un dataframe de foyers fiscaux :
                        # assert "idfoy" in input_dataframe.columns.to_list()
                        # FIX : si dataframe et openfisca indexent bien les individus dans leues foyers fiscaux
                        # de la même manière, on utilise openfisca pour aggréger les idfoy au niveau des foyers fiscaux
                        idfoy = self.simulations["baseline"].foyer_fiscal.members(
                            "idfoy", self.period
                        )
                        idfoy_simulation = (
                            self.simulations["baseline"]
                            .populations["foyer_fiscal"]
                            .members_entity_id
                        )  # dimension : individus
                        assert np.array_equal(
                            idfoy, idfoy_simulation
                        ), f"😈 Des indices de {entity} diffèrent entre le dataframe et la simulation : {idfoy - idfoy_simulation}"

                        idfoy_aggreges_foyer_fiscal = (
                            self.simulations["baseline"].populations["foyer_fiscal"].ids
                        )  # dimension : foyers fiscaux
                        input_dataframe[
                            "idfoy"
                        ] = idfoy_aggreges_foyer_fiscal  # TODO renommer ICI la colonne idfoy (variable d'individus normalement)

                    set_table_in_survey(
                        input_dataframe,
                        entity,
                        period=year,
                        collection=collection,
                        survey_name=survey_name,
                    )
        else:
            data_frame_by_entity = self.simulations[
                "baseline"
            ].create_data_frame_by_entity(variables=variables, period=period)

            for entity, input_dataframe in data_frame_by_entity.items():
                set_table_in_survey(
                    input_dataframe,
                    entity,
                    period=period,
                    collection=collection,
                    survey_name=survey_name,
                )

    def custom_input_data_frame(self, input_data_frame, entity=None, **kwargs):
        return
