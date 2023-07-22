from . import *


class Etape(Base):
    __tablename__ = 'etapes'

    id = Column(BigInteger, primary_key=True)
    roadbook_id = Column(BigInteger)
    evenement = Column(BigInteger)
    ordre = Column(BigInteger)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
    agence_id = Column(BigInteger)
    distance = Column(Float(asdecimal=True))
    heure_depart = Column(Text)
    heure_arrivee = Column(Text)

