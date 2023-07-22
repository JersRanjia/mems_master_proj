from data_generator.services import ModelService
from data_generator.models.models_pgsql.account_account import AccountAccount
from sqlalchemy import select


class AccountAccountService(ModelService):

    def create_all_account_account(self):
        # acc1 = AccountAccount(
        #     # name=
        # )
        pass

    def get_all_account_account_by_id(self, ids):
        stmt = select(AccountAccount)
        if ids:
            stmt = stmt.where(AccountAccount.id.in_(ids))

        out = self.db_service.pgsql_stmt_exec(stmt).fetchall()
        return out

