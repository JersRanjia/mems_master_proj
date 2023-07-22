from . import *


class Vehicule(Base):
    __tablename__ = 'vehicules'

    id = Column(BigInteger, primary_key=True)
    carrosserie_id = Column(BigInteger)
    numero = Column(Text)
    marque = Column(Text)
    serie = Column(Text)
    charge_utile = Column(BigInteger)
    volume = Column(BigInteger)
    consommation = Column(Float(asdecimal=True))
    vitesse = Column(Float(asdecimal=True))
    cv = Column(Float(asdecimal=True))
    places = Column(BigInteger)
    energie = Column(BigInteger)
    actif = Column(BigInteger)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
    agence_id = Column(Float(asdecimal=True))
