import logging
import numpy as np
from openfisca_core import reforms
from openfisca_core.errors import VariableNameConflictError
from openfisca_france_data import france_data_tax_benefit_system
from openfisca_france_data.model.base import (
    ADD,
    ETERNITY,
    YEAR,
    Individu,
    Menage,
    FoyerFiscal,
    Variable,
)


log = logging.getLogger(__name__)

neutralized_variables = [
    # Neutralisation de variables composantes du traitement indicidaire car elles ne sont pas identifiables dans les données ERFS-FPR
    "indemnite_residence",
    "supplement_familial_traitement",
    "indemnite_compensatrice_csg",
    # TH
    "taxe_habitation",
]


class leximpact_tbs_extension(reforms.Reform):
    def apply(self):
        class quimen(Variable):
            is_period_size_independent = True
            value_type = int
            entity = Individu
            label = "Rôle dans le ménage"
            definition_period = ETERNITY

        class quifam(Variable):
            is_period_size_independent = True
            value_type = int
            entity = Individu
            label = "Rôle dans la famille"
            definition_period = ETERNITY

        class quifoy(Variable):
            is_period_size_independent = True
            value_type = int
            entity = Individu
            label = "Rôle dans le foyer fiscal"
            definition_period = ETERNITY

        class idmen(Variable):
            is_period_size_independent = True
            value_type = int
            entity = Individu
            label = "Identifiant ménage dans openfisca-france-data"
            definition_period = ETERNITY

        class idmen_original(Variable):
            is_period_size_independent = True
            value_type = int
            entity = Menage
            label = "Identifiant ménage dans erfs-fpr"
            definition_period = ETERNITY

        class idfam(Variable):
            is_period_size_independent = True
            value_type = int
            entity = Individu
            label = "Identifiant famille dans openfisca-france-data"
            definition_period = ETERNITY

        class idfoy(Variable):
            is_period_size_independent = True
            value_type = int
            entity = Individu
            label = "Identifiant foyer fiscal dans openfisca-france-data"
            definition_period = ETERNITY

        class menage_id(Variable):
            is_period_size_independent = True
            value_type = int
            entity = Individu
            label = "Identifiant ménage"  # dans openfisca-survey-manager ?
            definition_period = ETERNITY

        class famille_id(Variable):
            is_period_size_independent = True
            value_type = int
            entity = Individu
            label = "Identifiant famille"  # dans openfisca-survey-manager ?
            definition_period = ETERNITY

        class foyer_fiscal_id(Variable):
            is_period_size_independent = True
            value_type = int
            entity = Individu
            label = "Identifiant foyer fiscal"  # dans openfisca-survey-manager ?
            definition_period = ETERNITY

        class noindiv(Variable):
            is_period_size_independent = True
            value_type = str  # champ texte de 10 caractères
            entity = Individu
            label = "Identifiant des individus dans l'enquête ERFS-FPR de l'INSEE"
            definition_period = ETERNITY

        class rpns_imposables(Variable):
            value_type = float
            entity = Individu
            label = "Revenus imposables des professions non salariées individuels"
            definition_period = YEAR

            def formula(individu, period):
                rag = individu("rag", period)
                ric = individu("ric", period)
                rnc = individu("rnc", period)

                return rag + ric + rnc

        class rfr_plus_values_hors_rni(Variable):
            value_type = float
            entity = FoyerFiscal
            label = "Plus-values hors RNI entrant dans le calcul du revenu fiscal de référence (PV au barème, PV éxonérées ..)"
            definition_period = YEAR

            def formula_2018_01_01(foyer_fiscal, period):
                return foyer_fiscal("assiette_csg_plus_values", period)

        class plus_values_prelevement_forfaitaire_unique_ir(Variable):
            value_type = float
            entity = FoyerFiscal
            label = "Plus-values soumises au prélèvement forfaitaire unique (partie impôt sur le revenu)"
            reference = (
                "https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000036377422/"
            )
            definition_period = YEAR

            def formula_2018_01_01(foyer_fiscal, period):
                return foyer_fiscal("assiette_csg_plus_values", period)

        class iaidrdi(Variable):
            value_type = float
            entity = FoyerFiscal
            label = "Impôt après imputation des réductions d'impôt"
            definition_period = YEAR

            def formula(foyer_fiscal, period, parameters):
                """
                Impôt après imputation des réductions d'impôt
                """
                ip_net = foyer_fiscal("ip_net", period)
                reductions = foyer_fiscal("reductions", period)

                return np.maximum(0, ip_net - reductions)

        class reduction_effective(Variable):
            value_type = float
            entity = FoyerFiscal
            label = "Impôt après imputation des réductions d'impôt"
            definition_period = YEAR

            def formula(foyer_fiscal, period):
                """
                Impôt après imputation des réductions d'impôt
                """
                ip_net = foyer_fiscal("ip_net", period)
                reductions = foyer_fiscal("reductions", period)

                return np.where(ip_net - reductions >= 0, reductions, ip_net)

        class impot_revenu_total(Variable):
            value_type = float
            entity = FoyerFiscal
            label = "Impôt sur le revenu avec la partie pfu"
            definition_period = YEAR

            def formula(foyer_fiscal, period):
                irpp_economique = foyer_fiscal("irpp_economique", period)
                pfu = foyer_fiscal("prelevement_forfaitaire_unique_ir", period)

                return irpp_economique + pfu

        class rpns_autres_revenus(Variable):
            value_type = float
            entity = Individu
            label = "Autres revenus non salariés"
            definition_period = YEAR

            def formula(individu, period):
                return np.maximum(individu("rpns_imposables", period), 0)

        class rfr_par_part(Variable):
            value_type = float
            entity = FoyerFiscal
            label = "Revenu fiscal de référence par part"
            definition_period = YEAR

            def formula(foyer_fiscal, period):
                rfr = foyer_fiscal("rfr", period)
                nbptr = foyer_fiscal("nbptr", period)
                return rfr / nbptr

        variables = [
            famille_id,
            foyer_fiscal_id,
            idfam,
            idfoy,
            idmen_original,
            idmen,
            impot_revenu_total,
            menage_id,
            # noindiv,  Removed because creates a bug with dump/restore (it is an object and not an int or a float)
            quifam,
            quifoy,
            quimen,
            reduction_effective,
            rfr_par_part,
            iaidrdi,
            plus_values_prelevement_forfaitaire_unique_ir,
            rfr_plus_values_hors_rni,
            rpns_imposables,
            rpns_autres_revenus,
        ]

        # Adaptation de variables du fait des variables de revenus du capital imputées

        for variable in variables:
            if variable == Variable:
                continue
            try:
                self.add_variable(variable)
            except VariableNameConflictError:
                log.warning(
                    f"{variable.__name__} has been updated in leximpact-survey-scenario"
                )
                self.update_variable(variable)
        for neutralized_variable in neutralized_variables:
            log.info(f"Neutralizing {neutralized_variable}")
            if self.get_variable(neutralized_variable):
                self.neutralize_variable(neutralized_variable)
        # for updated_variable in updated_variables:
        #    self.update_variable(updated_variable)

        # Création de variables de l'entité individu projetées sur le foyer fiscal nécéssaires
        # au calcul de stats ventilées par RFR
        foyer_fiscal_projected_variables = [
            "csg_deductible_salaire",
            "csg_imposable_salaire",
            "csg_deductible_retraite",
            "csg_imposable_retraite",
            "csg_salaire",
            "csg_retraite",
        ]
        for variable in foyer_fiscal_projected_variables:
            class_name = f"{variable}_foyer_fiscal"
            label = f"{variable} agrégée à l'échelle du foyer fiscal"

            def projection_formula_creator(variable):
                def formula(foyer_fiscal, period):
                    result_i = foyer_fiscal.members(variable, period, options=[ADD])
                    result = foyer_fiscal.sum(result_i)
                    return result

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

            self.add_variable(variable_instance)
            del variable_instance


leximpact_tbs = leximpact_tbs_extension(france_data_tax_benefit_system)
