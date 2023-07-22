from data_generator.models import *


class AccountAccount(Base):
    __tablename__ = 'account_account'
    __table_args__ = (
        UniqueConstraint('code', 'company_id'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('account_account_id_seq'::regclass)"))
    name = Column(String, nullable=False, index=True)
    currency_id = Column(Integer)
    code = Column(String(64), index=True)
    deprecated = Column(Boolean)
    user_type_id = Column(Integer)
    internal_type = Column(String)
    internal_group = Column(String)
    reconcile = Column(Boolean)
    note = Column(Text)
    company_id = Column(Integer)
    group_id = Column(Integer)
    root_id = Column(Integer)
    is_off_balance = Column(Boolean)
    create_uid = Column(Integer)
    create_date = Column(DateTime)
    write_uid = Column(Integer)
    write_date = Column(DateTime)
    asset_model = Column(Integer)
    create_asset = Column(String)
    multiple_assets_per_line = Column(Boolean)