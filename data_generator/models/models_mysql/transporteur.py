from . import *


class Transporteur(Base):
    __tablename__ = 'transporteurs'

    id = Column(BigInteger, primary_key=True)
    nom = Column(Text)
    charge_min = Column(BigInteger)
    nombre_min = Column(Float(asdecimal=True))
    charge_max = Column(BigInteger)
    nombre_max = Column(Float(asdecimal=True))
    contact = Column(Text)
    telephone = Column(Text)
    actif = Column(BigInteger)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
