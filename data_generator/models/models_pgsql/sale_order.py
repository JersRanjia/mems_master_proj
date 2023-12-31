from data_generator.models import *


class SaleOrder(Base):
    __tablename__ = 'sale_order'

    id = Column(Integer, primary_key=True, server_default=text("nextval('sale_order_id_seq'::regclass)"))
    name = Column(String, nullable=False, index=True)
    origin = Column(String)
    client_order_ref = Column(String)
    reference = Column(String)
    state = Column(String, index=True)
    date_order = Column(DateTime, nullable=False, index=True)
    validity_date = Column(Date)
    require_signature = Column(Boolean)
    require_payment = Column(Boolean)
    create_date = Column(DateTime, index=True)
    user_id = Column(Integer, index=True)
    partner_id = Column(Integer, nullable=False, index=True)
    partner_invoice_id = Column(Integer, nullable=False)
    partner_shipping_id = Column(Integer, nullable=False)
    pricelist_id = Column(Integer, nullable=False)
    currency_id = Column(Integer)
    analytic_account_id = Column(ForeignKey('account_analytic_account.id', ondelete='SET NULL'))
    invoice_status = Column(String)
    note = Column(Text)
    amount_untaxed = Column(Numeric)
    amount_tax = Column(Numeric)
    amount_total = Column(Numeric)
    currency_rate = Column(Numeric)
    payment_term_id = Column(Integer)
    fiscal_position_id = Column(Integer)
    company_id = Column(Integer, nullable=False, index=True)
    team_id = Column(Integer)
    signed_by = Column(String)
    signed_on = Column(DateTime)
    commitment_date = Column(DateTime)
    show_update_pricelist = Column(Boolean)
    message_main_attachment_id = Column(Integer, index=True)
    access_token = Column(String)
    campaign_id = Column(Integer)
    source_id = Column(Integer)
    medium_id = Column(Integer)
    create_uid = Column(Integer)
    write_uid = Column(Integer)
    write_date = Column(DateTime)
    sale_order_template_id = Column(Integer)
    incoterm = Column(Integer)
    picking_policy = Column(String)
    warehouse_id = Column(Integer)
    procurement_group_id = Column(Integer)
    effective_date = Column(Date)
    carrier_id = Column(Integer)
    delivery_message = Column(String)
    delivery_rating_success = Column(Boolean)
    recompute_delivery_price = Column(Boolean)
    location_id = Column(Integer)
    location_dest_id = Column(Integer)
    transport_type = Column(String)
    delivery_method = Column(String)
    invoice_id = Column(Integer)
    sender_id = Column(Integer)
    circuit = Column(String)
    identifier = Column(String)
    is_posted = Column(String)
    can_invoice = Column(Boolean)
    date_invoice = Column(DateTime)

    analytic_account = relationship('AccountAnalyticAccount')
