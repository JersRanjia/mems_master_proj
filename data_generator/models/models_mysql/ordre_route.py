from . import *


class OrdreRoute(Base):
    __tablename__ = 'ordre_routes'

    id = Column(BigInteger, primary_key=True)
    destination_id = Column(BigInteger)
    numero = Column(Text)
    user_id = Column(BigInteger)
    arrived_at = Column(TIMESTAMP)
    departed_at = Column(TIMESTAMP)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
    statut = Column(BigInteger)
    tournee_id = Column(Float(asdecimal=True))
    depart_id = Column(BigInteger)
