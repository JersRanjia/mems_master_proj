from dataclasses import dataclass, field

from ..services.db_services import DbService


@dataclass
class ModelService:
    db_service: DbService
