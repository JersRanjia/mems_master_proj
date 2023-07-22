from data_generator.models import *


class ProductTemplate(Base):
    __tablename__ = 'product_template'

    id = Column(Integer, primary_key=True, server_default=text("nextval('product_template_id_seq'::regclass)"))
    name = Column(String, nullable=False, index=True)
    sequence = Column(Integer)
    description = Column(Text)
    description_purchase = Column(Text)
    description_sale = Column(Text)
    type = Column(String, nullable=False)
    categ_id = Column(ForeignKey('product_category.id', ondelete='RESTRICT'), nullable=False)
    list_price = Column(Numeric)
    volume = Column(Numeric)
    weight = Column(Numeric)
    sale_ok = Column(Boolean)
    purchase_ok = Column(Boolean)
    uom_id = Column(Integer, nullable=False)
    uom_po_id = Column(Integer, nullable=False)
    company_id = Column(Integer, index=True)
    active = Column(Boolean)
    color = Column(Integer)
    default_code = Column(String)
    can_image_1024_be_zoomed = Column(Boolean)
    has_configurable_attributes = Column(Boolean)
    message_main_attachment_id = Column(Integer, index=True)
    create_uid = Column(Integer)
    create_date = Column(DateTime)
    write_uid = Column(Integer)
    write_date = Column(DateTime)
    service_type = Column(String)
    sale_line_warn = Column(String, nullable=False)
    sale_line_warn_msg = Column(Text)
    expense_policy = Column(String)
    invoice_policy = Column(String)
    sale_delay = Column(Float(53))
    tracking = Column(String, nullable=False)
    description_picking = Column(Text)
    description_pickingout = Column(Text)
    description_pickingin = Column(Text)
    hs_code = Column(String)
    purchase_method = Column(String)
    purchase_line_warn = Column(String, nullable=False)
    purchase_line_warn_msg = Column(Text)
    service_to_purchase = Column(Boolean)
    delivery_type = Column(String)
    write_price_unit = Column(Boolean)

    categ = relationship('ProductCategory')