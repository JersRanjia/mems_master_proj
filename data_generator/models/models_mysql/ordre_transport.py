from . import *


class OrdreTransport(Base):
    __tablename__ = 'ordre_transports'

    id = Column(BigInteger, primary_key=True)
    numero = Column(Text)
    bon_livraison_id = Column(Float(asdecimal=True))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
    colis_id = Column(Text)
    user_id = Column(BigInteger)
    depart_id = Column(BigInteger)
    destination_id = Column(BigInteger)
    ol_id = Column(Float(asdecimal=True))
    agence_id = Column(BigInteger)
    arret_id = Column(Float(asdecimal=True))
    circuit_id = Column(Float(asdecimal=True))
    ol_charge_at = Column(TIMESTAMP)
    ol_decharge_at = Column(TIMESTAMP)
    ol_retour_at = Column(TIMESTAMP)
    synced_at = Column(TIMESTAMP)
