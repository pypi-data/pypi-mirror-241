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

        class prelevement_forfaitaire_unique_ir_plus_values(Variable):
            value_type = float
            entity = FoyerFiscal
            label = "Partie du prélèvement forfaitaire unique associée à l'impôt sur le revenu sur les plus values"
            reference = [
                "Article 28 de la Loi n° 2017-1837 du 30 décembre 2017 de finances pour 2018 (modifie art. 125 A, 125-0 A, 200 A et art. 117 quater du CGI)",
                "https://www.legifrance.gouv.fr/affichTexteArticle.do?idArticle=LEGIARTI000036377422&cidTexte=JORFTEXT000036339197",
            ]
            definition_period = YEAR

            def formula_2018_01_01(foyer_fiscal, period, parameters):
                P = parameters(
                    period
                ).taxation_capital.prelevement_forfaitaire.partir_2018

                plus_values_prelevement_forfaitaire_unique_ir = foyer_fiscal(
                    "plus_values_prelevement_forfaitaire_unique_ir", period
                )

                return (
                    -plus_values_prelevement_forfaitaire_unique_ir
                    * P.taux_prelevement_forfaitaire_rev_capital_eligibles_pfu_interets_dividendes_etc
                )

        class prelevement_forfaitaire_non_liberatoire(Variable):
            value_type = float
            entity = FoyerFiscal
            label = "Prélèvement forfaitaire non libératoire sur les revenus du capital"
            definition_period = YEAR

            def formula_2018_01_01(foyer_fiscal, period):
                """
                Adaptation d'Openfisca France pour notre simulation budgétaire
                Dans le PLF l'agrégats d'impôt sur le revenu net ne contient que le PFU relatif aux plus-values payé au moment de l'imposition annuelle des revenus en N+1
                Les autres revenus soumis au PFU sont prélevés à la source et sont comptabilisés dans la partie autres recettes fiscales.
                On met donc dans cette variables l'ensemble du pfu hors plus_values
                Attention dans les faits il y a un décalage temporel car ce sont les revenus N qui sont comptabilisé dans autres recettes fiscales,
                alors que la case 2CK correspond au crédit d'impôt de prélèvement sur les revenus N-1
                """
                prelevement_forfaitaire_unique_ir = foyer_fiscal(
                    "prelevement_forfaitaire_unique_ir", period
                )
                prelevement_forfaitaire_unique_ir_plus_values = foyer_fiscal(
                    "prelevement_forfaitaire_unique_ir_plus_values", period
                )

                return -(
                    prelevement_forfaitaire_unique_ir
                    - prelevement_forfaitaire_unique_ir_plus_values
                )

            def formula_2013_01_01(foyer_fiscal, period):
                """
                A partir des revenus de 2013, certains revenus du capital qui pouvaient
                profiter du prélèvement forfaitaire libératoire sont passés à l'imposition obligatoire au barème.
                Mais un prélèvement forfaitaire demeure à partir de 2013, pour éviter les trous de trésorerie
                (car un prélèvement forfaitaire est à la source). Ce prélèvement est non-libératoire : il
                correspond à un acompte d'impot_revenu_restant_a_payer, qui est donc déduit de l'impôt dû au moment du calcul de
                l'impôt final après déclaration des revenus
                """
                f2ck = foyer_fiscal("f2ck", period)

                return f2ck

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
            prelevement_forfaitaire_non_liberatoire,
            prelevement_forfaitaire_unique_ir_plus_values,
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
