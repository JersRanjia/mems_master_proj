from . import *


class Axe(Base):
    __tablename__ = 'axes'

    id = Column(BigInteger, primary_key=True)
    nom = Column(Text)
    created_at = Column(Text)
    updated_at = Column(Text)


