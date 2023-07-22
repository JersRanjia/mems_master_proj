from data_generator.models import *


class AccountAnalyticAccount(Base):
    __tablename__ = 'account_analytic_account'

    id = Column(Integer, primary_key=True, server_default=text("nextval('account_analytic_account_id_seq'::regclass)"))
    name = Column(String, nullable=False, index=True)
    code = Column(String, index=True)
    active = Column(Boolean)
    group_id = Column(Integer)
    company_id = Column(Integer)
    partner_id = Column(Integer)
    message_main_attachment_id = Column(Integer, index=True)
    create_uid = Column(Integer)
    create_date = Column(DateTime)
    write_uid = Column(Integer)
    write_date = Column(DateTime)
