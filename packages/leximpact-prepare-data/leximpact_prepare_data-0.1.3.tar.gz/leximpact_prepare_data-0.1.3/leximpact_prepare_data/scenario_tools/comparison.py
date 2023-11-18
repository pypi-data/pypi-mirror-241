#!/usr/bin/env python

import click
import logging
import numpy as np
import pandas as pd
from pathlib import PurePath
import pypandoc

from openfisca_france_data.erfs_fpr import REFERENCE_YEAR

from openfisca_france_data.comparator import AbstractComparator

from leximpact_prepare_data.pipeline_survey_scenario import (
    PipelineErfsSurveyScenario,
)

from leximpact_aggregates.aggregate import DataStructure, AggregateManager
from leximpact_common_python_libraries.config import Configuration

# from leximpact_socio_fisca_simu_etat.aggregates_read import Aggregate

log = logging.getLogger(__name__)


from openfisca_france_data.model.base import (
    ADD,
    Variable,
    FoyerFiscal,
    YEAR,
)


foyer_projected_variables = [
    "chomage_imposable",
    "retraite_imposable",
    "salaire_imposable",
]


class LeximpactErfsComparator(AbstractComparator):
    name = "leximpact"
    period = None
    annee_donnees = None
    copules_comparaison = False

    target_menage_projected_variables = [
        f"{menage_projected_variable}_menage"
        for menage_projected_variable in foyer_projected_variables
    ]

    def __init__(self, period, annee_donnees, copules_comparaison=False):
        self.period = period
        self.annee_donnees = annee_donnees
        self.copules_comparaison = copules_comparaison
        super().__init__()

    def compute_test_dataframes(self):
        input_dataframe_by_entity = None
        target_dataframe_by_entity = None

        return input_dataframe_by_entity, target_dataframe_by_entity

    def get_survey_scenario(self, data=None, survey_name=None):
        if self.survey_scenario is not None:
            return self.survey_scenario
        if survey_name is None:
            survey_name = f"leximpact_{self.annee_donnees}"

        survey_scenario = PipelineErfsSurveyScenario(
            period=self.period,
            annee_donnees=self.annee_donnees,
            collection="leximpact",
            survey_name=survey_name,
            data=data,
        )

        # survey_scenario.tax_benefit_system = survey_scenario.tax_benefit_systems['baseline']
        tbs = survey_scenario.tax_benefit_systems["baseline"]
        for variable in foyer_projected_variables:
            class_name = f"{variable}_foyer_fiscal"
            label = f"{variable} agrégée à l'échelle du ménage"

            def projection_formula_creator(variable):
                def formula(foyer_fiscal, period):
                    result_i = foyer_fiscal.members(variable, period, options=[ADD])
                    return foyer_fiscal.sum(result_i)

                formula.__name__ = "formula"
                return formula

            variable_instance = type(
                class_name,
                (Variable,),
                dict(
                    value_type=float,
                    entity=FoyerFiscal,
                    label=label,
                    definition_period=YEAR,
                    formula=projection_formula_creator(variable),
                ),
            )

            tbs.add_variable(variable_instance)
            del variable_instance

        self.survey_scenario = survey_scenario
        return survey_scenario

    def _build_target_tenth(self, survey_scenario, variables=None):
        if variables is None:
            variables = [
                "salaire_imposable",
            ]
        period = self.period
        year = period
        data_year = period

        config = Configuration(project_folder="leximpact-prepare-data")
        aggregate_manager = AggregateManager(
            aggregates_path=config.get("AGREGATS_PATH")
        )

        def df_dixieme_pote(variable, year):
            aggregate_manager.load_aggregate(
                "POTE", variable, year=str(year), data_structure="distribution_100"
            )

            for d in aggregate_manager.aggregate.data:
                if (
                    d.data_structure == DataStructure.DISTRIBUTION_100
                    and d.date == str(data_year)
                ):
                    df_deciles_pote = pd.DataFrame(d.values)
                    break

            df_deciles_pote = df_deciles_pote[
                ["lower_bound", "upper_bound", "bucket_count", "bucket_sum"]
            ]
            df_deciles_pote["dixiemes"] = np.where(
                df_deciles_pote.index >= 100, 100, df_deciles_pote.index
            )
            df_deciles_pote = df_deciles_pote.groupby("dixiemes").agg(
                {
                    "lower_bound": "min",
                    "upper_bound": "max",
                    "bucket_count": "sum",
                    "bucket_sum": "sum",
                }
            )
            df_deciles_pote = df_deciles_pote.loc[df_deciles_pote["bucket_sum"] != 0]
            df_deciles_pote.reset_index(inplace=True)
            df_deciles_pote["variable"] = variable

            return df_deciles_pote

        def df_dixieme_erfs(variable):
            negative_variables = ["irpp_economique"]
            entity = (
                survey_scenario.tax_benefit_systems["baseline"]
                .variables[variable]
                .entity.key
            )
            weight_variable = survey_scenario.weight_variable_by_entity[entity]
            df = pd.DataFrame(
                {
                    variable: survey_scenario.calculate_variable(
                        variable, period, simulation="baseline"
                    ),
                    weight_variable: survey_scenario.calculate_variable(
                        weight_variable, period, simulation="baseline"
                    ).astype(float),
                }
            )

            if variable in negative_variables:
                df[variable] = -df[variable]

            filtered_df = df.query(f"{variable} != 0").sort_values(
                variable, ascending=True
            )
            filtered_df["dixiemes"] = np.ceil(
                100.0
                * filtered_df[weight_variable].cumsum()
                / filtered_df[weight_variable].sum()
            ).astype(int)

            filtered_df["variable_weight"] = (
                filtered_df[variable] * filtered_df[weight_variable]
            )

            filtered_df = filtered_df.groupby("dixiemes").agg(
                bucket_count=(weight_variable, np.sum),
                lower_bound=(variable, np.min),
                upper_bound=(variable, np.max),
                bucket_sum=("variable_weight", np.sum),
            )

            filtered_df["dixiemes"] = range(1, len(filtered_df) + 1)
            filtered_df["variable"] = variable
            return filtered_df

        def df_dixieme_pote_sur_erfs(variable, dixiemes_pote):
            entity = (
                survey_scenario.tax_benefit_systems["baseline"]
                .variables[variable]
                .entity.key
            )
            weight_variable = survey_scenario.weight_variable_by_entity[entity]

            df = pd.DataFrame(
                {
                    variable: survey_scenario.calculate_variable(
                        variable, period, simulation="baseline"
                    ),
                    weight_variable: survey_scenario.calculate_variable(
                        weight_variable, period, simulation="baseline"
                    ),
                }
            )
            filtered_df = df.query(variable + " ! 0").sort_values(
                variable, ascending=True
            )
            print(f"{variable} : {dixiemes_pote}")
            filtered_df["dixiemes_pote"] = pd.cut(
                filtered_df[variable],
                dixiemes_pote,
                labels=range(1, 101),
                include_lowest=True,
            )
            filtered_df["variable_weight"] = (
                filtered_df[variable] * filtered_df[weight_variable]
            )

            filtered_df = filtered_df.groupby("dixiemes_pote").agg(
                bucket_count=(weight_variable, np.sum),
                lower_bound=(variable, np.min),
                upper_bound=(variable, np.max),
                bucket_sum=("variable_weight", np.sum),
            )
            filtered_df["dixiemes"] = range(1, 101)
            filtered_df["variable"] = variable
            return filtered_df

        df = pd.DataFrame()
        for variable in variables:
            df_deciles_pote = df_dixieme_pote(variable, year)
            df_variable = pd.concat(
                {
                    "dixiemes_pote": df_deciles_pote.set_index("dixiemes"),
                    "dixiemes_simulation": df_dixieme_erfs(variable).set_index(
                        "dixiemes"
                    ),
                    # "dixieme_pote_sur_simulation": df_dixieme_pote_sur_erfs(variable, df_deciles_pote.upper_bound).set_index("dixiemes"),
                },
                names=["origin", "dixiemes"],
            )

            df = pd.concat([df, df_variable])

        return df

    def _plot_tenth(self, df):
        import seaborn as sns

        figures_directory = self.figures_directory
        variables = df.variable.unique()
        markdown_sections = """
## Distibution comparison

"""
        print(variables)
        for variable in variables:
            print(df.query(f"variable == '{variable}'"))
            df_variable = df.query(f"variable == '{variable}'")[
                [
                    "lower_bound",
                    "bucket_count",
                    "bucket_sum",
                ]
            ].reset_index()

            column_by_prefix = {
                "decile": "lower_bound",
                "count": "bucket_count",
                "sum": "bucket_sum",
            }

            markdown_section = f"""
### Variable `{variable}`
"""
            for prefix, column in column_by_prefix.items():
                if prefix == "decile":
                    data = df_variable.pivot("dixiemes", "origin", column).dropna()
                    sns_plot = sns.lineplot(data=data).set_title(variable)
                else:
                    data = df_variable[["dixiemes", "origin", column]].dropna()
                    sns_plot = sns.barplot(
                        data=data, x="dixiemes", y=column, hue="origin"
                    ).set_title(variable)

                variable_pdf_path = PurePath.joinpath(
                    figures_directory, f"{prefix}_{variable}.pdf"
                )
                sns_plot.figure.savefig(variable_pdf_path)
                sns_plot.figure.clf()

                markdown_section += f"""
#### {prefix}

![]({variable_pdf_path})
"""
            markdown_sections += markdown_section

        return markdown_sections

    #####
    def _build_target_copules(self, survey_scenario, variables=None):
        if variables is None:
            variables = [
                "assiette_csg_revenus_capital",
            ]
        period = self.period
        year = period

        config = Configuration(project_folder="leximpact-prepare-data")
        aggregate_manager = AggregateManager(
            aggregates_path=config.get("AGREGATS_PATH")
        )

        def df_copules_pote(variable, year):
            if variable == "assiette_csg_plus_values":
                copules_var = "revenus_individuels"
                data_structure = "copulas_20"
            elif variable in ["credits_impot", "reductions"]:
                copules_var = "revkire_par_part"
                data_structure = "copulas_100"
            else:
                copules_var = "revenus_individuels"
                data_structure = "copulas_100"
            aggregate_manager.load_aggregate(
                "POTE",
                variable,
                year=str(year),
                data_structure=data_structure,
                copules_var=copules_var,
            )
            df_copules_pote = pd.DataFrame(aggregate_manager.aggregate.data[-1].values)

            df_copules_pote["part_nonzero"] = (
                df_copules_pote["count_nonzero"] / df_copules_pote["count"]
            )
            df_copules_pote["somme"] = [
                df_copules_pote["buckets"][i][0]["bucket_sum"]
                + df_copules_pote["buckets"][i][0]["sum_above_upper_bound"]
                for i in range(len(df_copules_pote))
            ]
            df_copules_pote = df_copules_pote[["count", "part_nonzero", "somme"]]
            df_copules_pote["copules"] = range(len(df_copules_pote))
            df_copules_pote["variable"] = variable
            return df_copules_pote

        def df_copules_erfs(variable, nb_copules_pote=None):
            if variable == "assiette_csg_plus_values":
                copules_var = "revenus_individuels"
                nb_copules = 19
            elif variable in ["credits_impot", "reductions"]:
                copules_var = "revkire_par_part"
                nb_copules = 99
            else:
                copules_var = "revenus_individuels"
                nb_copules = 99

            negative_variables = ["irpp_economique"]

            entity = (
                survey_scenario.tax_benefit_systems["baseline"]
                .variables[variable]
                .entity.key
            )
            weight_variable = survey_scenario.weight_variable_by_entity[entity]
            df = pd.DataFrame(
                {
                    variable: survey_scenario.calculate_variable(
                        variable, period, simulation="baseline"
                    ),
                    weight_variable: survey_scenario.calculate_variable(
                        weight_variable, period, simulation="baseline"
                    ).astype(float),
                    copules_var: survey_scenario.calculate_variable(
                        copules_var, period, simulation="baseline"
                    ),
                }
            )

            if variable in negative_variables:
                df[variable] = -df[variable]

            if nb_copules_pote is not None:
                nb_copules = nb_copules_pote - 1

            df["variable_pond"] = df[variable] * df[weight_variable]
            df["variable_nonnulle"] = (df[variable] != 0) * df[weight_variable]
            df_zero = df.loc[df[copules_var] == 0]
            df_zero["copules"] = 0
            df_nonzero = df.loc[df[copules_var] != 0].sort_values(
                copules_var, ascending=True
            )
            df_nonzero["copules"] = np.minimum(
                np.ceil(
                    nb_copules
                    * df_nonzero[weight_variable].cumsum()
                    / df_nonzero[weight_variable].sum()
                ),
                nb_copules,
            )
            df = pd.concat([df_zero, df_nonzero])
            df = df.groupby("copules").agg(
                {
                    "variable_pond": "sum",
                    "variable_nonnulle": "sum",
                    weight_variable: "sum",
                }
            )
            df.rename(
                columns={weight_variable: "count", "variable_pond": "somme"},
                inplace=True,
            )
            df["part_nonzero"] = df["variable_nonnulle"] / df["count"]
            df["copules"] = range(nb_copules + 1)
            df["variable"] = variable

            return df[["count", "part_nonzero", "somme", "copules", "variable"]]

        df = pd.DataFrame()
        for variable in variables:
            df_pote = df_copules_pote(variable, year)
            df_variable = pd.concat(
                {
                    "copules_pote": df_pote.set_index("copules"),
                    "copules_simulation": df_copules_erfs(
                        variable, nb_copules_pote=len(df_pote)
                    ).set_index("copules"),
                },
                names=["origin", "copules"],
            )

            df = pd.concat([df, df_variable])

        return df

    def _plot_copules(self, df):
        import seaborn as sns

        figures_directory = self.figures_directory
        variables = df.variable.unique()
        markdown_sections = """
## Copules distribution comparison

"""
        print(variables)
        for variable in variables:
            print(df.query(f"variable == '{variable}'"))
            df_variable = df.query(f"variable == '{variable}'").reset_index()

            column_by_prefix = ["count", "part_nonzero", "somme"]

            markdown_section = f"""
### Variable `{variable}`
"""
            for column in column_by_prefix:
                data = df_variable[["copules", "origin", column]].dropna()
                sns_plot = sns.barplot(
                    data=data, x="copules", y=column, hue="origin"
                ).set_title(variable)

                variable_pdf_path = PurePath.joinpath(
                    figures_directory, f"copules_{column}_{variable}.pdf"
                )
                sns_plot.figure.savefig(variable_pdf_path)
                sns_plot.figure.clf()

                markdown_section += f"""
#### {column}

![]({variable_pdf_path})
"""
            markdown_sections += markdown_section

        return markdown_sections

    ####

    def compute_distibution_comparison(self, input_dataframe_by_entity=None):
        survey_scenario = self.get_survey_scenario()

        df = self._build_target_tenth(survey_scenario, variables=self.target_variables)
        markdown_sections_distrib = self._plot_tenth(df)
        if self.copules_comparaison:
            df = self._build_target_copules(
                survey_scenario, variables=self.target_variables
            )
            markdown_sections_copules = self._plot_copules(df)
            markdown_sections = markdown_sections_distrib + markdown_sections_copules
        else:
            markdown_sections = markdown_sections_distrib
        figures_directory = self.figures_directory
        with open(
            figures_directory / "distribution_comparison_md", "w", encoding="utf-8"
        ) as distribution_comparison_md_file:
            distribution_comparison_md_file.write(markdown_sections)

    def compute_aggregates_comparison(self, input_dataframe_by_entity=None):
        variable_pote_by_variable = {
            # "chomage_imposable": "chomage_et_indemnites",
            # "retraite_imposable": "retraites",
            # "salaire_imposable": "rev_salaire",
        }
        tenth_variable_pote_by_variable = {
            "chomage_imposable": "chomage_et_indemnites",
            "retraite_imposable": "retraite_imposable",
            "salaire_imposable": "salaire_imposable",
            "assiette_csg_plus_values": "assiette_csg_plus_values",
            "assiette_csg_revenus_capital": "assiette_csg_revenus_capital",
            "credits_impot": "credits_impot",
            "reductions": "reductions",
            "charges_deduc": "charges_deduc",
            "revenu_categoriel_foncier": "revenu_categoriel_foncier",
            "revenus_capitaux_prelevement_forfaitaire_unique_ir": "revenus_capitaux_prelevement_forfaitaire_unique_ir",
            "rente_viagere_titre_onereux_net": "rente_viagere_titre_onereux_net",
            "revenus_capitaux_prelevement_bareme": "revenus_capitaux_prelevement_bareme",
            "revenus_capitaux_prelevement_liberatoire": "revenus_capitaux_prelevement_liberatoire",
            # "irpp_economique": "irpp_economique",
            "revenus_individuels": "revenus_individuels",
            "rfr": "rfr",
            "rpns_imposables": "rpns_imposables",
        }
        period = self.period
        figures_directory = self.figures_directory

        def summarize_variable_from_pote_tenth(variable):
            variable_pote = tenth_variable_pote_by_variable[variable]
            config = Configuration(project_folder="leximpact-prepare-data")
            aggregate_manager = AggregateManager(
                aggregates_path=config.get("AGREGATS_PATH")
            )
            aggregate_manager.load_aggregate(
                "POTE",
                variable_pote,
                year=str(period),
                data_structure="distribution_100",
            )

            for d in aggregate_manager.aggregate.data:
                if (
                    d.data_structure == DataStructure.DISTRIBUTION_100
                    and d.date == str(period)
                ):
                    df_deciles_pote = pd.DataFrame(d.values)
                    break

            df_deciles_pote = df_deciles_pote[
                ["lower_bound", "upper_bound", "bucket_count", "bucket_sum"]
            ]

            summary = dict()
            nb_foy_pote = df_deciles_pote.bucket_count.sum()
            summary["sum"] = df_deciles_pote.bucket_sum.sum()
            summary["mean"] = summary["sum"] / nb_foy_pote
            summary["lenzero"] = df_deciles_pote.loc[
                df_deciles_pote["bucket_sum"] == 0
            ].bucket_count.sum()
            summary["pct_zero"] = summary["lenzero"] / nb_foy_pote
            summary["mean_excluding_zeros"] = summary["sum"] / (
                nb_foy_pote - summary["lenzero"]
            )
            summary["count_non_zero"] = nb_foy_pote - summary["lenzero"]
            summary["source"] = "POTE"
            summary["variable"] = variable
            return summary

        def summarize_variable_from_pote(variable):
            config = Configuration(project_folder="leximpact-prepare-data")
            aggregate_manager = AggregateManager(
                aggregates_path=config.get("AGREGATS_PATH")
            )

            variable_pote = variable_pote_by_variable[variable]
            values = ["sum", "mean", "lenzero", "pct_zero"]
            summary = dict()
            for value in values:
                summary[value] = aggregate_manager.get_aggregate_value(
                    dataset="POTE", var=variable_pote, year=str(period), agg_type=value
                )

            nb_foy_pote = summary["lenzero"] / (summary["pct_zero"] / 100)
            summary["mean_excluding_zeros"] = summary["sum"] / (
                nb_foy_pote - summary["lenzero"]
            )
            summary["count_non_zero"] = nb_foy_pote - summary["lenzero"]
            summary["source"] = "POTE"
            summary["variable"] = variable
            summary["pct_zero"] = summary["pct_zero"] / 100
            return summary

        def summarize_variable(variable, survey_scenario, period, source="simulation"):
            summary = dict()
            for aggfunc in ["sum", "mean", "count_non_zero"]:
                if variable in foyer_projected_variables:
                    summary[aggfunc] = survey_scenario.simulations[
                        "baseline"
                    ].compute_aggregate(
                        f"{variable}_foyer_fiscal",
                        aggfunc=aggfunc,
                        period=period,
                    )
                else:
                    summary[aggfunc] = survey_scenario.simulations[
                        "baseline"
                    ].compute_aggregate(
                        variable,
                        aggfunc=aggfunc,
                        period=period,
                    )
            if variable in foyer_projected_variables:
                summary["lenzero"] = (
                    survey_scenario.simulations["baseline"].compute_aggregate(
                        f"{variable}_foyer_fiscal", aggfunc="count", period=period
                    )
                    - summary["count_non_zero"]
                )
                nb_tot = survey_scenario.simulations["baseline"].compute_aggregate(
                    f"{variable}_foyer_fiscal", aggfunc="count", period=period
                )
            else:
                summary["lenzero"] = (
                    survey_scenario.simulations["baseline"].compute_aggregate(
                        variable, aggfunc="count", period=period
                    )
                    - summary["count_non_zero"]
                )
                nb_tot = survey_scenario.simulations["baseline"].compute_aggregate(
                    variable, aggfunc="count", period=period
                )

            summary["mean_excluding_zeros"] = summary["sum"] / summary["count_non_zero"]
            summary["pct_zero"] = 1 - summary["count_non_zero"] / nb_tot

            summary["variable"] = variable
            summary["source"] = "simulation"
            return summary

        survey_scenario = self.get_survey_scenario()

        records = (
            [
                summarize_variable_from_pote(variable)
                for variable in variable_pote_by_variable.keys()
            ]
            + [
                summarize_variable(variable, survey_scenario, period)
                for variable in variable_pote_by_variable.keys()
            ]
            + [
                summarize_variable_from_pote_tenth(variable)
                for variable in self.target_variables
            ]
            + [
                summarize_variable(variable, survey_scenario, period)
                for variable in self.target_variables
            ]
        )

        df = (
            pd.DataFrame.from_records(records)
            .sort_values(["variable", "source"])
            .set_index(["variable", "source"])
        )

        aggregates_table = pd.DataFrame(index=df.index)
        aggregates_table["Masse (Md€)"] = (df["sum"] / 1e9).round(0).astype(int)
        aggregates_table["Moyenne (€)"] = df["mean"].astype(int)
        aggregates_table["Moyenne hors nuls (€)"] = df["mean_excluding_zeros"].astype(
            int
        )
        aggregates_table["Effectifx (milliers)"] = (
            (df["count_non_zero"] / 1e3).round(0).astype(int)
        )
        aggregates_table["Part des nuls (%)"] = (df["pct_zero"] * 100).astype(int)

        aggregates_table.reset_index(inplace=True)
        aggregates_table_markdown_path = PurePath.joinpath(
            figures_directory, "table_agregats.md"
        )
        aggregates_table.to_markdown(aggregates_table_markdown_path, index=False)

        pypandoc.convert_file(
            str(aggregates_table_markdown_path),
            "pdf",
            format="markdown",
            outputfile=str(PurePath.joinpath(figures_directory, "table_agregats.pdf")),
            extra_args=["--pdf-engine=pdflatex"],
        )

        return aggregates_table


@click.command()
@click.option(
    "-b",
    "--browse",
    is_flag=True,
    help="Browse results",
    default=False,
    show_default=True,
)
@click.option(
    "-l",
    "--load",
    is_flag=True,
    default=False,
    help="Load backup results",
    show_default=True,
)
@click.option(
    "-v",
    "--verbose",
    is_flag=True,
    default=False,
    help="Increase aggregates_table verbosity",
    show_default=True,
)
@click.option(
    "-d",
    "--debug",
    is_flag=True,
    default=False,
    help="Use python debugger",
    show_default=True,
)
@click.option(
    "-p",
    "--period",
    default=REFERENCE_YEAR,
    help="period(s) to treat",
    show_default=True,
)
@click.option(
    "-t",
    "--target-variables",
    default=None,
    help="target variables to inspect (None means all)",
    show_default=True,
)
@click.option(
    "-u",
    "--rebuild",
    is_flag=True,
    default=False,
    help="Rebuild test data",
    show_default=True,
)
@click.option(
    "-s",
    "--summary",
    is_flag=True,
    default=False,
    help="Produce summary figuress",
    show_default=True,
)
def compare(
    browse=False,
    load=False,
    verbose=True,
    debug=True,
    target_variables=None,
    period=None,
    rebuild=False,
    summary=False,
):
    """Compare openfisca-france-data simulation to erfs-fpr by generating comparison data and graphs.

    Data can be explored using D-Tale and graphs are saved as pdf files.
    """
    comparator = LeximpactErfsComparator()
    comparator.period = period

    comparator.compare(
        browse, load, verbose, debug, target_variables, period, rebuild, summary
    )
