from . import *


class Circuit(Base):
    __tablename__ = 'circuits'

    id = Column(BigInteger, primary_key=True)
    agence_id = Column(BigInteger)
    nom = Column(Text)
    direction = Column(Text)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)