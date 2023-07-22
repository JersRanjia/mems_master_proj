from dataclasses import dataclass, field
from typing import Any, Union

import sqlalchemy
from sqlalchemy.engine.mock import MockConnection
from sqlalchemy.future import Engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import Session


@dataclass
class DbManager:
    login_conf: dict
    engine: Union[Union[MockConnection, Engine], Any] = field(init=False)

    def __post_init__(self):
        engine = sqlalchemy.create_engine(
            # sqlalchemy.engine.make_url(**self.login_conf)
            URL.create(**self.login_conf)
        )

        self.session = Session(engine, autocommit=True)
        self.engine = engine

    def clear_tables(self):
        pass

    def init_tables(self):
        pass
