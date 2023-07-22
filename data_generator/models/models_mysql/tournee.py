from . import *


class Tournee(Base):
    __tablename__ = 'tournees'

    id = Column(BigInteger, primary_key=True)
    depart_id = Column(BigInteger)
    vehicule_id = Column(Float(asdecimal=True))
    transporteur_id = Column(Float(asdecimal=True))
    chauffeur1_id = Column(BigInteger)
    chauffeur2_id = Column(Float(asdecimal=True))
    type_transport = Column(BigInteger)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
    destination_id = Column(BigInteger)
    numero = Column(Text)
    statut = Column(BigInteger)
