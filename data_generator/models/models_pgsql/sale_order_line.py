from data_generator.models import *


class SaleOrderLine(Base):
    __tablename__ = 'sale_order_line'

    id = Column(Integer, primary_key=True, server_default=text("nextval('sale_order_line_id_seq'::regclass)"))
    order_id = Column(ForeignKey('sale_order.id', ondelete='CASCADE'), nullable=False, index=True)
    name = Column(Text, nullable=False)
    sequence = Column(Integer)
    invoice_status = Column(String)
    price_unit = Column(Numeric, nullable=False)
    price_subtotal = Column(Numeric)
    price_tax = Column(Float(53))
    price_total = Column(Numeric)
    price_reduce = Column(Numeric)
    price_reduce_taxinc = Column(Numeric)
    price_reduce_taxexcl = Column(Numeric)
    discount = Column(Numeric)
    product_id = Column(Integer)
    product_uom_qty = Column(Numeric, nullable=False)
    product_uom = Column(Integer)
    qty_delivered_method = Column(String)
    qty_delivered = Column(Numeric)
    qty_delivered_manual = Column(Numeric)
    qty_to_invoice = Column(Numeric)
    qty_invoiced = Column(Numeric)
    untaxed_amount_invoiced = Column(Numeric)
    untaxed_amount_to_invoice = Column(Numeric)
    salesman_id = Column(Integer)
    currency_id = Column(Integer)
    company_id = Column(Integer, index=True)
    order_partner_id = Column(Integer)
    is_expense = Column(Boolean)
    is_downpayment = Column(Boolean)
    state = Column(String)
    customer_lead = Column(Float(53))
    display_type = Column(String)
    create_uid = Column(Integer)
    create_date = Column(DateTime)
    write_uid = Column(Integer)
    write_date = Column(DateTime)
    product_packaging = Column(Integer)
    route_id = Column(Integer)
    is_delivery = Column(Boolean)
    value = Column(Float(53))
    real_weight = Column(Float(53))
    volume_weight = Column(Float(53))
    weighing_id = Column(Integer)
    delivery_rate_id = Column(Integer)
    packaging_rate_id = Column(Integer)
    handling_rate_id = Column(Integer)
    handling_rate = Column(Float(53))
    packaging_rate = Column(Float(53))
    qr_in_report = Column(Boolean)
    parent_order_line_id = Column(ForeignKey('sale_order_line.id', ondelete='SET NULL'))
    ref_colis = Column(String)
    quantity = Column(Integer)
    copied = Column(Boolean)
    duplicata = Column(Boolean)
    orig_quantity = Column(Integer)
    price_unit_def = Column(Float(53))
    etat_livraison_moved0 = Column(Boolean)
    date_livraison = Column(DateTime)
    type_of = Column(String)
    etat_livraison = Column(String)

    order = relationship('SaleOrder')
    parent_order_line = relationship('SaleOrderLine', remote_side=[id])
