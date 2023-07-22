import json
from typing import List

from ..db_manager.db_managers import DbManager
from ..utils import singleton
from sqlalchemy.engine.result import ScalarResult

class DbService(metaclass=singleton.SingletonMeta):
    pgsqlManager: DbManager
    mysqlManager: DbManager

    def __init__(self) -> None:

        with open(r"D:\ketrika\mems_proj\data_generator\config\login_pgsql.json", "r") as f:
            login_conf = json.load(f)
            self.pgsqlManager = DbManager(login_conf)

        with open(r"D:\ketrika\mems_proj\data_generator\config\login_mysql.json", "r") as f:
            login_conf = json.load(f)
            self.mysqlManager = DbManager(login_conf)

    def __enter__(self):
        self.pgsql_transac = self.pgsqlManager.session.begin()
        self.mysql_transac = self.mysqlManager.session.begin()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.pgsql_transac.__exit__(None, None, None)
        self.pgsqlManager.session.close()
        self.pgsql_transac.__exit__(None, None, None)
        self.mysqlManager.session.close()

    def begin_session(self):
        self.pgsql_transac = self.pgsqlManager.session.begin()
        self.mysql_transac = self.mysqlManager.session.begin()

    def close_session(self):
        self.pgsql_transac.__exit__(None, None, None)
        self.pgsqlManager.session.close()
        self.pgsql_transac.__exit__(None, None, None)
        self.mysqlManager.session.close()

    def pgsql_add(self, model_instance):
        self.pgsqlManager.session.add(model_instance)
        # self.pgsqlManager.session.get

    def pgsql_add_all(self, model_instance_list):
        self.pgsqlManager.session.add_all(model_instance_list)

    def pgsql_stmt_exec(self, stmt) -> ScalarResult:
        return self.pgsqlManager.session.scalars(stmt)

    def mysql_add(self, model_instance):
        self.mysqlManager.session.add(model_instance)

    def mysql_add_all(self, model_instance_list):
        self.mysqlManager.session.add_all(model_instance_list)


