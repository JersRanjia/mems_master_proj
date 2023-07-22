from . import *


class Agence(Base):
    __tablename__ = 'agences'

    id = Column(BigInteger, primary_key=True)
    agence_id = Column(Float(asdecimal=True))
    zone = Column(BigInteger)
    nom = Column(Text)
    sigle = Column(Text)
    capacite = Column(Float(asdecimal=True))
    actif = Column(BigInteger)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
    axe_id = Column(Float(asdecimal=True))
    count_or = Column(BigInteger)
    count_ot = Column(BigInteger)
    count_anomalies = Column(BigInteger)
    count_incidents = Column(BigInteger)
    count_transbordements = Column(BigInteger)
    count_ol = Column(BigInteger)
    count_bl = Column(BigInteger)
    count_os = Column(BigInteger)
    count_tr = Column(BigInteger)
    count_retour = Column(BigInteger)