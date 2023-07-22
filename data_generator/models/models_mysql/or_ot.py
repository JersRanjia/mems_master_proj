from . import *


class OrOt(Base):
    __tablename__ = 'or_ot'

    id = Column(BigInteger, primary_key=True)
    or_id = Column(BigInteger)
    ot_id = Column(BigInteger)
    charge_at = Column(TIMESTAMP)
    decharge_at = Column(TIMESTAMP)
