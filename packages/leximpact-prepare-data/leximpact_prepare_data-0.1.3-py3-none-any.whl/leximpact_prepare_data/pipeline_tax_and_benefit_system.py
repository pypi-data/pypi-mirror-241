import logging
from openfisca_core import reforms
from numpy import where

from openfisca_core.populations import ADD
from openfisca_core.holders import set_input_dispatch_by_period
from openfisca_france_data.model.base import (
    YEAR,
    MONTH,
    Menage,
    FoyerFiscal,
    Individu,
    Variable,
)

from leximpact_survey_scenario.leximpact_tax_and_benefit_system import leximpact_tbs

log = logging.getLogger(__name__)


class revenus_individuels(Variable):
    value_type = float
    entity = FoyerFiscal
    label = "Somme des revenus individuels utilisés pour l'imputation des revenus du capital"
    definition_period = YEAR

    def formula(foyer_fiscal, period):
        salaire_imposable_i = foyer_fiscal.members(
            "salaire_imposable", period, options=[ADD]
        )
        salaire_imposable = foyer_fiscal.sum(salaire_imposable_i)
        retraite_imposable_i = foyer_fiscal.members(
            "retraite_imposable", period, options=[ADD]
        )
        retraite_imposable = foyer_fiscal.sum(retraite_imposable_i)
        chomage_imposable_i = foyer_fiscal.members(
            "chomage_imposable", period, options=[ADD]
        )
        chomage_imposable = foyer_fiscal.sum(chomage_imposable_i)
        rpns_imposables_i = foyer_fiscal.members("rpns_imposables", period)
        rpns_imposables = foyer_fiscal.sum(rpns_imposables_i)
        pensions_invalidite_i = foyer_fiscal.members(
            "pensions_invalidite", period, options=[ADD]
        )
        pensions_invalidite = foyer_fiscal.sum(pensions_invalidite_i)
        pensions_alimentaires_percues_i = foyer_fiscal.members(
            "pensions_alimentaires_percues", period, options=[ADD]
        )
        pensions_alimentaires_percues = foyer_fiscal.sum(
            pensions_alimentaires_percues_i
        )

        return (
            salaire_imposable
            + retraite_imposable
            + chomage_imposable
            + rpns_imposables
            + pensions_invalidite
            + pensions_alimentaires_percues
        )


class revenus_individuels_par_part(Variable):
    value_type = float
    entity = FoyerFiscal
    label = "Somme des revenus individuels utilisés pour l'imputation des revenus du capital"
    definition_period = YEAR

    def formula(foyer_fiscal, period):
        revenus_individuels = foyer_fiscal("revenus_individuels", period)
        nbptr = foyer_fiscal("nbptr", period)

        return revenus_individuels / nbptr


class revkire_par_part(Variable):
    value_type = float
    entity = FoyerFiscal
    label = "Revenu fiscal de référence par part, pour l imputation des réductions et crédits d impot"
    definition_period = YEAR

    def formula(foyer_fiscal, period):
        revenus_individuels = foyer_fiscal("rfr", period)
        nbptr = foyer_fiscal("nbptr", period)

        return revenus_individuels / nbptr


class prest_precarite_hand(Variable):
    value_type = float
    default_value = 1.0
    entity = Menage
    label = "Montant des minima liés au handicap dans l'erfs-fpr. Utilisé pour imputer un taux de handicap dans la simulation"
    definition_period = YEAR
    is_period_size_independent = True
    set_input = set_input_dispatch_by_period


class revenus_minimum_menage(Variable):
    value_type = bool
    default_value = False
    entity = Individu
    label = "Variable intermédiaire dans le calcul de l'aah qui désigne la personne du couple principal ayant les plus faibles revenus"
    definition_period = YEAR


class taux_capacite_travail(Variable):
    value_type = float
    default_value = 1.0
    entity = Individu
    label = "Taux de capacité de travail, appréciée par la commission des droits et de l'autonomie des personnes handicapées (CDAPH)"
    definition_period = MONTH
    is_period_size_independent = True
    set_input = set_input_dispatch_by_period

    def formula(individu, period):
        prest_precarite_hand_menage = individu.menage(
            "prest_precarite_hand", period.start.year
        )
        revenus_minimum_menage = individu("revenus_minimum_menage", period.start.year)
        return where((prest_precarite_hand_menage > 0) & revenus_minimum_menage, 0.1, 1)
        # return where(prest_precarite_hand_menage > 0, 0.1,1)


class taux_incapacite(Variable):
    value_type = float
    entity = Individu
    label = "Taux d'incapacité pris en compte pour l'AAH"
    definition_period = MONTH
    reference = "https://www.legifrance.gouv.fr/affichCodeArticle.do;jsessionid=BD54F4B28313142C87FC8B96013E0441.tplgfr44s_1?idArticle=LEGIARTI000023097719&cidTexte=LEGITEXT000006073189&dateTexte=20190312"
    documentation = (
        "Taux d'incapacité pris en compte pour l'allocation adulte handicapé (AAH)."
    )
    is_period_size_independent = True
    set_input = set_input_dispatch_by_period
    unit = "/1"

    def formula(individu, period):
        prest_precarite_hand_menage = individu.menage(
            "prest_precarite_hand", period.start.year
        )
        revenus_minimum_menage = individu("revenus_minimum_menage", period.start.year)
        return where(
            (prest_precarite_hand_menage > 0) & revenus_minimum_menage, 0.81, 0
        )
        # return where(prest_precarite_hand_menage > 0, 0.81,0)


variables = [
    revenus_individuels,
    revenus_individuels_par_part,
    revkire_par_part,
    prest_precarite_hand,
    revenus_minimum_menage,
]

variables_to_update = [taux_capacite_travail, taux_incapacite]


class pipeline_tbs_extension(reforms.Reform):
    def apply(self):
        for variable in variables:
            if variable == Variable:
                continue
            try:
                self.add_variable(variable)
            except AttributeError:
                self.update_variable(variable)
        for variable in variables_to_update:
            self.update_variable(variable)


pipeline_tbs = pipeline_tbs_extension(leximpact_tbs)
