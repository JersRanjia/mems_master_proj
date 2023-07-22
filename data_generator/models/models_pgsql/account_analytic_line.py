from data_generator.models import *
from datetime import datetime

class AccountAnalyticLine(Base):
    __tablename__ = 'account_analytic_line'

    id = Column(Integer, primary_key=True, server_default=text("nextval('account_analytic_line_id_seq'::regclass)"))
    name = Column(String, nullable=False)
    date = Column(Date, nullable=False, index=True)
    amount = Column(Numeric, nullable=False)
    unit_amount = Column(Float(53))
    product_uom_id = Column(Integer)
    account_id = Column(ForeignKey('account_analytic_account.id', ondelete='RESTRICT'), nullable=False, index=True)
    partner_id = Column(Integer)
    user_id = Column(Integer)
    currency_id = Column(Integer)
    group_id = Column(Integer)
    create_uid = Column(Integer)
    create_date = Column(DateTime, default=datetime.now())
    write_uid = Column(Integer)
    write_date = Column(DateTime)
    product_id = Column(Integer)
    general_account_id = Column(ForeignKey('account_account.id', ondelete='RESTRICT'))
    move_id = Column(Integer, index=True)
    code = Column(String(8))
    ref = Column(String)
    # so_line = Column(ForeignKey('sale_order_line.id', ondelete='SET NULL'), nullable=True)
    so_line = Column(Integer)
    account = relationship('AccountAnalyticAccount')
    general_account = relationship('AccountAccount')
    # sale_order_line = relationship('SaleOrderLine')
