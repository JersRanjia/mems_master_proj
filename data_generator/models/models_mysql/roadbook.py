from . import *


class Roadbook(Base):
    __tablename__ = 'roadbooks'

    id = Column(BigInteger, primary_key=True)
    depart_id = Column(BigInteger)
    destination_id = Column(BigInteger)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
    transport = Column(BigInteger)