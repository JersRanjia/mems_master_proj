create table account_account
(
    id serial not null
        constraint account_account_pkey
            primary key,
    name varchar not null,
    currency_id integer,
    code varchar(64) not null,
    deprecated boolean,
    user_type_id integer not null,
    internal_type varchar,
    internal_group varchar,
    reconcile boolean,
    note text,
    company_id integer not null,
    group_id integer,
    root_id integer,
    is_off_balance boolean,
    create_uid integer,
    create_date timestamp,
    write_uid integer,
    write_date timestamp,
    asset_model integer,
    create_asset varchar not null,
    multiple_assets_per_line boolean,
    constraint account_account_code_company_uniq
        unique (code, company_id)
);

alter table account_account owner to postgres;

create index account_account_code_index
    on account_account (code);

create index account_account_deprecated_index
    on account_account (deprecated);

create index account_account_name_index
    on account_account (name);

create table account_analytic_account
(
    id serial not null
        constraint account_analytic_account_pkey
            primary key,
    name varchar not null,
    code varchar,
    active boolean,
    group_id integer,
    company_id integer,
    partner_id integer,
    message_main_attachment_id integer,
    create_uid integer,
    create_date timestamp,
    write_uid integer,
    write_date timestamp
);

alter table account_analytic_account owner to postgres;

create index account_analytic_account_code_index
    on account_analytic_account (code);

create index account_analytic_account_message_main_attachment_id_index
    on account_analytic_account (message_main_attachment_id);

create index account_analytic_account_name_index
    on account_analytic_account (name);

create table product_category
(
    id serial not null
        constraint product_category_pkey
            primary key,
    name varchar not null,
    complete_name varchar,
    parent_id integer
        constraint product_category_parent_id_fkey
            references product_category
            on delete cascade,
    parent_path varchar,
    create_uid integer,
    create_date timestamp,
    write_uid integer,
    write_date timestamp,
    removal_strategy_id integer
);

alter table product_category owner to postgres;

create index product_category_name_index
    on product_category (name);

create index product_category_parent_id_index
    on product_category (parent_id);

create index product_category_parent_path_index
    on product_category (parent_path);

create table product_template
(
    id serial not null
        constraint product_template_pkey
            primary key,
    name varchar not null,
    sequence integer,
    description text,
    description_purchase text,
    description_sale text,
    type varchar not null,
    categ_id integer not null
        constraint product_template_categ_id_fkey
            references product_category
            on delete restrict,
    list_price numeric,
    volume numeric,
    weight numeric,
    sale_ok boolean,
    purchase_ok boolean,
    uom_id integer not null,
    uom_po_id integer not null,
    company_id integer,
    active boolean,
    color integer,
    default_code varchar,
    can_image_1024_be_zoomed boolean,
    has_configurable_attributes boolean,
    message_main_attachment_id integer,
    create_uid integer,
    create_date timestamp,
    write_uid integer,
    write_date timestamp,
    service_type varchar,
    sale_line_warn varchar not null,
    sale_line_warn_msg text,
    expense_policy varchar,
    invoice_policy varchar,
    sale_delay double precision,
    tracking varchar not null,
    description_picking text,
    description_pickingout text,
    description_pickingin text,
    hs_code varchar,
    purchase_method varchar,
    purchase_line_warn varchar not null,
    purchase_line_warn_msg text,
    service_to_purchase boolean,
    delivery_type varchar,
    write_price_unit boolean
);

alter table product_template owner to postgres;

create index product_template_company_id_index
    on product_template (company_id);

create index product_template_message_main_attachment_id_index
    on product_template (message_main_attachment_id);

create index product_template_name_index
    on product_template (name);

create table sale_order
(
    id serial not null
        constraint sale_order_pkey
            primary key,
    name varchar not null,
    origin varchar,
    client_order_ref varchar,
    reference varchar,
    state varchar,
    date_order timestamp not null,
    validity_date date,
    require_signature boolean,
    require_payment boolean,
    create_date timestamp,
    user_id integer,
    partner_id integer not null,
    partner_invoice_id integer not null,
    partner_shipping_id integer not null,
    pricelist_id integer not null,
    currency_id integer,
    analytic_account_id integer
        constraint sale_order_analytic_account_id_fkey
            references account_analytic_account
            on delete set null,
    invoice_status varchar,
    note text,
    amount_untaxed numeric,
    amount_tax numeric,
    amount_total numeric,
    currency_rate numeric,
    payment_term_id integer,
    fiscal_position_id integer,
    company_id integer not null,
    team_id integer,
    signed_by varchar,
    signed_on timestamp,
    commitment_date timestamp,
    show_update_pricelist boolean,
    message_main_attachment_id integer,
    access_token varchar,
    campaign_id integer,
    source_id integer,
    medium_id integer,
    create_uid integer,
    write_uid integer,
    write_date timestamp,
    sale_order_template_id integer,
    incoterm integer,
    picking_policy varchar not null,
    warehouse_id integer not null,
    procurement_group_id integer,
    effective_date date,
    carrier_id integer,
    delivery_message varchar,
    delivery_rating_success boolean,
    recompute_delivery_price boolean,
    location_id integer,
    location_dest_id integer,
    transport_type varchar,
    delivery_method varchar,
    invoice_id integer,
    sender_id integer,
    circuit varchar,
    identifier varchar,
    is_posted varchar,
    can_invoice boolean,
    date_invoice timestamp
);

alter table sale_order owner to postgres;

create index sale_order_company_id_index
    on sale_order (company_id);

create index sale_order_create_date_index
    on sale_order (create_date);

create index sale_order_date_order_index
    on sale_order (date_order);

create index sale_order_message_main_attachment_id_index
    on sale_order (message_main_attachment_id);

create index sale_order_name_index
    on sale_order (name);

create index sale_order_partner_id_index
    on sale_order (partner_id);

create index sale_order_state_index
    on sale_order (state);

create index sale_order_user_id_index
    on sale_order (user_id);

create table sale_order_line
(
    id serial not null
        constraint sale_order_line_pkey
            primary key,
    order_id integer not null
        constraint sale_order_line_order_id_fkey
            references sale_order
            on delete cascade,
    name text not null,
    sequence integer,
    invoice_status varchar,
    price_unit numeric not null,
    price_subtotal numeric,
    price_tax double precision,
    price_total numeric,
    price_reduce numeric,
    price_reduce_taxinc numeric,
    price_reduce_taxexcl numeric,
    discount numeric,
    product_id integer,
    product_uom_qty numeric not null,
    product_uom integer,
    qty_delivered_method varchar,
    qty_delivered numeric,
    qty_delivered_manual numeric,
    qty_to_invoice numeric,
    qty_invoiced numeric,
    untaxed_amount_invoiced numeric,
    untaxed_amount_to_invoice numeric,
    salesman_id integer,
    currency_id integer,
    company_id integer,
    order_partner_id integer,
    is_expense boolean,
    is_downpayment boolean,
    state varchar,
    customer_lead double precision not null,
    display_type varchar,
    create_uid integer,
    create_date timestamp,
    write_uid integer,
    write_date timestamp,
    product_packaging integer,
    route_id integer,
    is_delivery boolean,
    value double precision,
    real_weight double precision,
    volume_weight double precision,
    weighing_id integer,
    delivery_rate_id integer,
    packaging_rate_id integer,
    handling_rate_id integer,
    handling_rate double precision,
    packaging_rate double precision,
    qr_in_report boolean,
    parent_order_line_id integer
        constraint sale_order_line_parent_order_line_id_fkey
            references sale_order_line
            on delete set null,
    ref_colis varchar,
    quantity integer,
    copied boolean,
    duplicata boolean,
    orig_quantity integer,
    price_unit_def double precision,
    etat_livraison_moved0 boolean,
    date_livraison timestamp,
    type_of varchar,
    etat_livraison varchar
);

alter table sale_order_line owner to postgres;

create index sale_order_line_company_id_index
    on sale_order_line (company_id);

create index sale_order_line_order_id_index
    on sale_order_line (order_id);

create table account_analytic_line
(
    id serial not null
        constraint account_analytic_line_pkey
            primary key,
    name varchar not null,
    date date not null,
    amount numeric not null,
    unit_amount double precision,
    product_uom_id integer,
    account_id integer not null
        constraint account_analytic_line_account_id_fkey
            references account_analytic_account
            on delete restrict,
    partner_id integer,
    user_id integer,
    currency_id integer,
    group_id integer,
    create_uid integer,
    create_date timestamp,
    write_uid integer,
    write_date timestamp,
    product_id integer,
    general_account_id integer
        constraint account_analytic_line_general_account_id_fkey
            references account_account
            on delete restrict,
    move_id integer,
    code varchar(8),
    ref varchar,
    so_line integer
        constraint account_analytic_line_so_line_fkey
            references sale_order_line
            on delete set null
);

alter table account_analytic_line owner to postgres;

create index account_analytic_line_account_id_index
    on account_analytic_line (account_id);

create index account_analytic_line_date_index
    on account_analytic_line (date);

create index account_analytic_line_move_id_index
    on account_analytic_line (move_id);

