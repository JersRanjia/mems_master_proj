from data_generator.models import *


class ProductCategory(Base):
    __tablename__ = 'product_category'

    id = Column(Integer, primary_key=True, server_default=text("nextval('product_category_id_seq'::regclass)"))
    name = Column(String, nullable=False, index=True)
    complete_name = Column(String)
    parent_id = Column(ForeignKey('product_category.id', ondelete='CASCADE'), index=True)
    parent_path = Column(String, index=True)
    create_uid = Column(Integer)
    create_date = Column(DateTime)
    write_uid = Column(Integer)
    write_date = Column(DateTime)
    removal_strategy_id = Column(Integer)

    parent = relationship('ProductCategory', remote_side=[id])
