-- we don't know how to generate root <with-no-name> (class Root) :(
create table agences
(
	id bigint auto_increment PRIMARY KEY,
	agence_id double null,
	zone bigint null,
	nom text null,
	sigle text null,
	capacite double null,
	actif bigint null,
	created_at timestamp null,
	updated_at timestamp null,
	axe_id double null,
	count_or bigint null,
	count_ot bigint null,
	count_anomalies bigint null,
	count_incidents bigint null,
	count_transbordements bigint null,
	count_ol bigint null,
	count_bl bigint null,
	count_os bigint null,
	count_tr bigint null,
	count_retour bigint null
);

create table agents
(
	id bigint auto_increment PRIMARY KEY,
	matricule text null,
	agence_id double null,
	nom text null,
	prenom text null,
	telephone text null,
	user_id double null,
	created_at timestamp null,
	updated_at timestamp null,
	actif bigint null
);

create table axes
(
	id bigint auto_increment PRIMARY KEY,
	nom text null,
	created_at text null,
	updated_at text null
);

create table circuits
(
	id bigint auto_increment PRIMARY KEY,
	agence_id bigint null,
	nom text null,
	direction text null,
	created_at timestamp null,
	updated_at timestamp null
);

create table colis
(
	id bigint auto_increment PRIMARY KEY,
	numero_bc text null,
	numero_article text null,
	depart_id bigint null,
	destination_id bigint null,
	client_id double null,
	type_envoi bigint null,
	mode_livraison bigint null,
	mode_transport bigint null,
	mode_paiement bigint null,
	libelle text null,
	agent text null,
	description text null,
	quantite double null,
	longueur bigint null,
	largeur bigint null,
	hauteur bigint null,
	poids bigint null,
	expediteur_nom text null,
	expediteur_adresse text null,
	expediteur_tel text null,
	destinataire_nom text null,
	destinataire_adresse text null,
	destinataire_tel text null,
	date_reception timestamp null,
	created_at timestamp null,
	updated_at timestamp null,
	observation text null,
	document text null,
	valeur_declaree double null,
	delai double null,
	circuit text null,
	finance text null,
	note text null
);

create table etapes
(
	id bigint auto_increment PRIMARY KEY,
	roadbook_id bigint null,
	evenement bigint null,
	ordre bigint null,
	created_at timestamp null,
	updated_at timestamp null,
	agence_id bigint null,
	distance double null,
	heure_depart text null,
	heure_arrivee text null
);

create table evenements
(
	id bigint auto_increment PRIMARY KEY,
	ot_id bigint null,
	user_id bigint null,
	eventable_type bigint null,
	eventable_id bigint null,
	created_at timestamp null,
	agence_id bigint null,
	statut bigint null,
	arret_id double null
);

create table or_ot
(
	id bigint auto_increment PRIMARY KEY,
	or_id bigint null,
	ot_id bigint null,
	charge_at timestamp null,
	decharge_at timestamp null
);

create table ordre_livraisons
(
	id bigint auto_increment PRIMARY KEY,
	numero text null,
	user_id bigint null,
	circuit_id double null,
	agence_id bigint null,
	vehicule_id double null,
	chauffeur_id double null,
	transporteur_id double null,
	depart_at timestamp null,
	created_at timestamp null,
	updated_at timestamp null,
	is_sortie bigint null,
	planifiee_at timestamp null,
	arrivee_at timestamp null
);

create table ordre_routes
(
	id bigint auto_increment PRIMARY KEY,
	destination_id bigint null,
	numero text null,
	user_id bigint null,
	arrived_at timestamp null,
	departed_at timestamp null,
	created_at timestamp null,
	updated_at timestamp null,
	statut bigint null,
	tournee_id double null,
	depart_id bigint null
);

create table ordre_transports
(
	id bigint auto_increment PRIMARY KEY,
	numero text null,
	bon_livraison_id double null,
	created_at timestamp null,
	updated_at timestamp null,
	colis_id text null,
	user_id bigint null,
	depart_id bigint null,
	destination_id bigint null,
	ol_id double null,
	agence_id bigint null,
	arret_id double null,
	circuit_id double null,
	ol_charge_at timestamp null,
	ol_decharge_at timestamp null,
	ol_retour_at timestamp null,
	synced_at timestamp null
);

create table roadbooks
(
	id bigint auto_increment PRIMARY KEY,
	depart_id bigint null,
	destination_id bigint null,
	created_at timestamp null,
	updated_at timestamp null,
	transport bigint null
);

create table tournees
(
	id bigint auto_increment PRIMARY KEY,
	depart_id bigint null,
	vehicule_id double null,
	transporteur_id double null,
	chauffeur1_id bigint null,
	chauffeur2_id double null,
	type_transport bigint null,
	created_at timestamp null,
	updated_at timestamp null,
	destination_id bigint null,
	numero text null,
	statut bigint null
);

create table transporteurs
(
	id bigint auto_increment PRIMARY KEY,
	nom text null,
	charge_min bigint null,
	nombre_min double null,
	charge_max bigint null,
	nombre_max double null,
	contact text null,
	telephone text null,
	actif bigint null,
	created_at timestamp null,
	updated_at timestamp null
);

create table vehicules
(
	id bigint auto_increment PRIMARY KEY,
	carrosserie_id bigint null,
	numero text null,
	marque text null,
	serie text null,
	charge_utile bigint null,
	volume bigint null,
	consommation double null,
	vitesse double null,
	cv double null,
	places bigint null,
	energie bigint null,
	actif bigint null,
	created_at timestamp null,
	updated_at timestamp null,
	agence_id double null
);

