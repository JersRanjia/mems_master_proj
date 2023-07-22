from .services.db_services import DbService
from data_generator.services.services_pgsql.account_analytic_account_service import *
from data_generator.services.services_pgsql.account_analytic_line import *
from data_generator.services.services_pgsql.account_account_service import *


def seed_odoo_db(db_service: DbService):

    aaa_service = AccountAnalyticAccountService(db_service)
    aa_service = AccountAccountService(db_service)
    aal_service = AccountAnalyticLineService(db_service)

    aa_list = aa_service.get_all_account_account_by_id(list(set(DEPENSE_LABELS.values())))
    aaa_list = aaa_service.gen_aaa_vehicle_model()

    aal_list = aal_service.generate_aal(aaa_list, aa_list)

    db_service.pgsql_add_all(aal_list)


def seed_op_db(db_service: DbService):


    pass


if __name__ == '__main__':

    with DbService() as db_service:
        # seccompte = AccountAccount(
        #     name="secondcompte"
        # )
        # aaa = AccountAnalyticAccount(
        #     name="1010",
        #     group_id=5
        # )
        # aal = AccountAnalyticLine(
        #     name="blabla",
        #     amount=1500,
        #     account=aaa,
        #     general_account=seccompte,
        #     date=datetime.now()
        # )
        # db_service.pgsql_add(aal)

        # vehicle_models = gen_aaa_vehicle_model()
        # db_service.pgsql_add_all(vehicle_models)

        # seed_odoo_db(db_service)
        pass