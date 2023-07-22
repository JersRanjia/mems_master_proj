from . import *


class Evenement(Base):
    __tablename__ = 'evenements'

    id = Column(BigInteger, primary_key=True)
    ot_id = Column(BigInteger)
    user_id = Column(BigInteger)
    eventable_type = Column(BigInteger)
    eventable_id = Column(BigInteger)
    created_at = Column(TIMESTAMP)
    agence_id = Column(BigInteger)
    statut = Column(BigInteger)
    arret_id = Column(Float(asdecimal=True))
