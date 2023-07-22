from . import *


class Colis(Base):
    __tablename__ = 'colis'

    id = Column(BigInteger, primary_key=True)
    numero_bc = Column(Text)
    numero_article = Column(Text)
    depart_id = Column(BigInteger)
    destination_id = Column(BigInteger)
    client_id = Column(Float(asdecimal=True))
    type_envoi = Column(BigInteger)
    mode_livraison = Column(BigInteger)
    mode_transport = Column(BigInteger)
    mode_paiement = Column(BigInteger)
    libelle = Column(Text)
    agent = Column(Text)
    description = Column(Text)
    quantite = Column(Float(asdecimal=True))
    longueur = Column(BigInteger)
    largeur = Column(BigInteger)
    hauteur = Column(BigInteger)
    poids = Column(BigInteger)
    expediteur_nom = Column(Text)
    expediteur_adresse = Column(Text)
    expediteur_tel = Column(Text)
    destinataire_nom = Column(Text)
    destinataire_adresse = Column(Text)
    destinataire_tel = Column(Text)
    date_reception = Column(TIMESTAMP)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
    observation = Column(Text)
    document = Column(Text)
    valeur_declaree = Column(Float(asdecimal=True))
    delai = Column(Float(asdecimal=True))
    circuit = Column(Text)
    finance = Column(Text)
    note = Column(Text)
