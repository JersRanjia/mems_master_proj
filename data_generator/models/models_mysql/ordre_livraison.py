from . import *


class OrdreLivraison(Base):
    __tablename__ = 'ordre_livraisons'

    id = Column(BigInteger, primary_key=True)
    numero = Column(Text)
    user_id = Column(BigInteger)
    circuit_id = Column(Float(asdecimal=True))
    agence_id = Column(BigInteger)
    vehicule_id = Column(Float(asdecimal=True))
    chauffeur_id = Column(Float(asdecimal=True))
    transporteur_id = Column(Float(asdecimal=True))
    depart_at = Column(TIMESTAMP)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
    is_sortie = Column(BigInteger)
    planifiee_at = Column(TIMESTAMP)
    arrivee_at = Column(TIMESTAMP)