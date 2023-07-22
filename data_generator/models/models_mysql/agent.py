from . import *


class Agent(Base):
    __tablename__ = 'agents'

    id = Column(BigInteger, primary_key=True)
    matricule = Column(Text)
    agence_id = Column(Float(asdecimal=True))
    nom = Column(Text)
    prenom = Column(Text)
    telephone = Column(Text)
    user_id = Column(Float(asdecimal=True))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
    actif = Column(BigInteger)
