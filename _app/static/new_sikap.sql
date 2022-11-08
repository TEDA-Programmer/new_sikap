--
-- PostgreSQL database dump
--

-- Dumped from database version 12.12
-- Dumped by pg_dump version 14.5 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: uuid-ossp; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS "uuid-ossp" WITH SCHEMA public;


--
-- Name: EXTENSION "uuid-ossp"; Type: COMMENT; Schema: -; Owner:
--

COMMENT ON EXTENSION "uuid-ossp" IS 'generate universally unique identifiers (UUIDs)';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: agen; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.agen (
    id character varying DEFAULT public.uuid_generate_v4() NOT NULL,
    nama_agen character varying,
    alamat_agen character varying,
    telepon_agen character varying,
    fax_agen character varying,
    email_agen character varying,
    pic_agen character varying,
    ket character varying,
    add_by character varying,
    add_time timestamp without time zone
);


ALTER TABLE public.agen OWNER TO postgres;

--
-- Name: assist_tug; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.assist_tug (
    id character varying DEFAULT public.uuid_generate_v4() NOT NULL,
    shipment_id character varying,
    jenis_assist_id integer,
    nama_tugboat1 character varying,
    master_tugboat1 character varying,
    start_time1 timestamp without time zone,
    end_time1 timestamp without time zone,
    nama_tugboat2 character varying,
    master_tugboat2 character varying,
    start_time2 timestamp without time zone,
    end_time2 timestamp without time zone,
    nama_pandu character varying,
    naik_time timestamp without time zone,
    turun_time timestamp without time zone,
    add_by character varying,
    add_time timestamp without time zone,
    nama_debitur character varying,
    alamat character varying,
    biaya_politage integer,
    total integer
);


ALTER TABLE public.assist_tug OWNER TO postgres;

--
-- Name: auth; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth (
    id integer NOT NULL,
    auth_name character varying
);


ALTER TABLE public.auth OWNER TO postgres;

--
-- Name: auth_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_id_seq OWNER TO postgres;

--
-- Name: auth_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_id_seq OWNED BY public.auth.id;


--
-- Name: form_anchorage; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.form_anchorage (
    id character varying DEFAULT public.uuid_generate_v4() NOT NULL,
    tr_shipment_status_id character varying,
    time_arrival_anchorage timestamp without time zone,
    eta_berthed date,
    est_complete_sts date,
    balance_unloading_sts integer,
    add_by character varying,
    add_time timestamp without time zone,
    ket character varying
);


ALTER TABLE public.form_anchorage OWNER TO postgres;

--
-- Name: form_berthed; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.form_berthed (
    id character varying DEFAULT public.uuid_generate_v4() NOT NULL,
    tr_shipment_status_id character varying,
    time_from_anchorage timestamp without time zone,
    time_berthed timestamp without time zone,
    nor_tendered timestamp without time zone,
    nor_accepted timestamp without time zone,
    commence_discharge timestamp without time zone,
    est_completed date,
    est_cast_of date,
    add_by character varying,
    add_time timestamp without time zone,
    ket character varying
);


ALTER TABLE public.form_berthed OWNER TO postgres;

--
-- Name: form_cast_of_jetty; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.form_cast_of_jetty (
    id character varying DEFAULT public.uuid_generate_v4() NOT NULL,
    tr_shipment_status_id character varying,
    cast_of_jetty timestamp without time zone,
    commence_completed timestamp without time zone,
    final_draught_survey numeric,
    add_by character varying,
    add_time timestamp without time zone,
    ket character varying
);


ALTER TABLE public.form_cast_of_jetty OWNER TO postgres;

--
-- Name: form_onasiling; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.form_onasiling (
    id character varying DEFAULT public.uuid_generate_v4() NOT NULL,
    tr_shipment_status_id character varying,
    time_departure date,
    eta_anchorage date,
    add_by character varying,
    add_time timestamp without time zone,
    ket character varying
);


ALTER TABLE public.form_onasiling OWNER TO postgres;

--
-- Name: form_onasiling_tongkang_sts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.form_onasiling_tongkang_sts (
    id character varying DEFAULT public.uuid_generate_v4() NOT NULL,
    tr_shipment_status_id character varying,
    arrival_at_anchorage timestamp without time zone,
    tender_at_vessel timestamp without time zone,
    commance_loading_disch timestamp without time zone,
    completed_loading_disch timestamp without time zone,
    total_loading_mt integer,
    loading_area character varying,
    add_by character varying,
    add_time timestamp without time zone,
    ket character varying
);


ALTER TABLE public.form_onasiling_tongkang_sts OWNER TO postgres;

--
-- Name: form_shifting_in; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.form_shifting_in (
    id character varying DEFAULT public.uuid_generate_v4() NOT NULL,
    tr_shipment_status_id character varying,
    time_shifting_in timestamp without time zone,
    add_by character varying,
    add_time timestamp without time zone,
    ket character varying
);


ALTER TABLE public.form_shifting_in OWNER TO postgres;

--
-- Name: form_shifting_out; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.form_shifting_out (
    id character varying DEFAULT public.uuid_generate_v4() NOT NULL,
    tr_shipment_status_id character varying,
    time_shifting_out timestamp without time zone,
    add_by character varying,
    add_time timestamp without time zone,
    ket character varying
);


ALTER TABLE public.form_shifting_out OWNER TO postgres;

--
-- Name: jenis_assist_tug; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.jenis_assist_tug (
    id integer NOT NULL,
    jenis_name character varying,
    ket character varying
);


ALTER TABLE public.jenis_assist_tug OWNER TO postgres;

--
-- Name: jenis_assist_tug_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.jenis_assist_tug_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.jenis_assist_tug_id_seq OWNER TO postgres;

--
-- Name: jenis_assist_tug_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.jenis_assist_tug_id_seq OWNED BY public.jenis_assist_tug.id;


--
-- Name: pltu; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pltu (
    id character varying DEFAULT public.uuid_generate_v4() NOT NULL,
    pltu_name character varying,
    capacity integer,
    area character varying,
    cabang character varying,
    kode character varying,
    regional character varying,
    delete_status integer DEFAULT 0
);


ALTER TABLE public.pltu OWNER TO postgres;

--
-- Name: shipment; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.shipment (
    id character varying DEFAULT public.uuid_generate_v4() NOT NULL,
    capt_kapal character varying,
    shipper_id character varying,
    agen_id character varying,
    bl_number character varying,
    muatan_cargo_bl integer,
    pelabuhan_muat character varying,
    ket character varying
);


ALTER TABLE public.shipment OWNER TO postgres;

--
-- Name: shipment_docs; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.shipment_docs (
    id character varying DEFAULT public.uuid_generate_v4() NOT NULL,
    shipment_id character varying,
    doc_filename character varying,
    add_by character varying,
    add_time character varying,
    shipment_status character varying,
    ket character varying
);


ALTER TABLE public.shipment_docs OWNER TO postgres;

--
-- Name: shipment_service; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.shipment_service (
    id character varying DEFAULT public.uuid_generate_v4() NOT NULL,
    shipment_id character varying,
    agent integer DEFAULT 0,
    assist_tug integer DEFAULT 0,
    sts integer DEFAULT 0,
    jetty_management integer DEFAULT 0,
    pbm integer DEFAULT 0,
    add_by character varying,
    add_time timestamp without time zone
);


ALTER TABLE public.shipment_service OWNER TO postgres;

--
-- Name: shipment_status; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.shipment_status (
    id integer NOT NULL,
    status_name character varying,
    key character varying
);


ALTER TABLE public.shipment_status OWNER TO postgres;

--
-- Name: shipment_status_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.shipment_status_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.shipment_status_id_seq OWNER TO postgres;

--
-- Name: shipment_status_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.shipment_status_id_seq OWNED BY public.shipment_status.id;


--
-- Name: shipment_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.shipment_type (
    id integer NOT NULL,
    type_name character varying,
    ket character varying
);


ALTER TABLE public.shipment_type OWNER TO postgres;

--
-- Name: shipment_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.shipment_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.shipment_type_id_seq OWNER TO postgres;

--
-- Name: shipment_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.shipment_type_id_seq OWNED BY public.shipment_type.id;


--
-- Name: shipper; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.shipper (
    id character varying DEFAULT public.uuid_generate_v4() NOT NULL,
    nama_shipper character varying,
    alamat_shipper character varying,
    telepon_shipper character varying,
    fax_shipper character varying,
    email_shipper character varying,
    pic_shipper character varying,
    ket character varying,
    add_by character varying,
    add_time timestamp without time zone
);


ALTER TABLE public.shipper OWNER TO postgres;

--
-- Name: spb; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.spb (
    id character varying DEFAULT public.uuid_generate_v4() NOT NULL,
    nama_spb character varying,
    pemilik_spb character varying,
    bendera character varying,
    kelas character varying,
    tahun integer,
    grt integer,
    dwt integer,
    nrt integer,
    loa integer,
    sarat_muka character varying,
    sarat_belakang character varying,
    ket character varying,
    add_by character varying,
    add_time timestamp without time zone
);


ALTER TABLE public.spb OWNER TO postgres;

--
-- Name: tongkang; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tongkang (
    id character varying DEFAULT public.uuid_generate_v4() NOT NULL,
    nama_tongkang character varying,
    pemilik_tongkang character varying,
    bendera character varying,
    kelas character varying,
    tahun integer,
    grt integer,
    dwt integer,
    nrt integer,
    loa integer,
    sarat_muka character varying,
    sarat_belakang character varying,
    ket character varying,
    add_by character varying,
    add_time timestamp without time zone
);


ALTER TABLE public.tongkang OWNER TO postgres;

--
-- Name: tr_shipment_status; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tr_shipment_status (
    id character varying DEFAULT public.uuid_generate_v4() NOT NULL,
    shipment_id character varying,
    status_id integer,
    add_by character varying,
    add_time character varying,
    pltu_tujuan_deviasi integer
);


ALTER TABLE public.tr_shipment_status OWNER TO postgres;

--
-- Name: tr_shipment_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tr_shipment_type (
    id character varying DEFAULT public.uuid_generate_v4() NOT NULL,
    shipment_id character varying,
    type_id integer,
    tugboat_id character varying,
    tongkang_id character varying,
    vessel_id character varying,
    spb_id character varying,
    shipment_sts_id character varying
);


ALTER TABLE public.tr_shipment_type OWNER TO postgres;

--
-- Name: tugboat; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tugboat (
    id character varying DEFAULT public.uuid_generate_v4() NOT NULL,
    nama_tugboat character varying,
    pemilik_tugboat character varying,
    ket character varying,
    add_by character varying,
    add_time timestamp without time zone
);


ALTER TABLE public.tugboat OWNER TO postgres;

--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id character varying DEFAULT public.uuid_generate_v4() NOT NULL,
    auth_id integer,
    username character varying,
    hashed_password character varying,
    nama character varying,
    email character varying,
    grup character varying,
    area character varying,
    opr character varying,
    cabang character varying,
    delete_status integer DEFAULT 0,
    add_by character varying,
    add_time timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: vessel; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.vessel (
    id character varying DEFAULT public.uuid_generate_v4() NOT NULL,
    nama_vessel character varying,
    pemilik_vessel character varying,
    bendera character varying,
    kelas character varying,
    tahun integer,
    grt integer,
    dwt integer,
    nrt integer,
    loa integer,
    sarat_muka character varying,
    sarat_belakang character varying,
    ket character varying,
    add_by character varying,
    add_time timestamp without time zone
);


ALTER TABLE public.vessel OWNER TO postgres;

--
-- Name: auth id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth ALTER COLUMN id SET DEFAULT nextval('public.auth_id_seq'::regclass);


--
-- Name: jenis_assist_tug id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jenis_assist_tug ALTER COLUMN id SET DEFAULT nextval('public.jenis_assist_tug_id_seq'::regclass);


--
-- Name: shipment_status id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shipment_status ALTER COLUMN id SET DEFAULT nextval('public.shipment_status_id_seq'::regclass);


--
-- Name: shipment_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shipment_type ALTER COLUMN id SET DEFAULT nextval('public.shipment_type_id_seq'::regclass);


--
-- Data for Name: agen; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: assist_tug; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: auth; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.auth (id, auth_name) VALUES (1, 'Administrator');
INSERT INTO public.auth (id, auth_name) VALUES (2, 'Regional');
INSERT INTO public.auth (id, auth_name) VALUES (3, 'PLTU');
INSERT INTO public.auth (id, auth_name) VALUES (4, 'Cabang');


--
-- Data for Name: form_anchorage; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: form_berthed; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: form_cast_of_jetty; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: form_onasiling; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: form_onasiling_tongkang_sts; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: form_shifting_in; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: form_shifting_out; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: jenis_assist_tug; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: pltu; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: shipment; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: shipment_docs; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: shipment_service; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: shipment_status; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: shipment_type; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: shipper; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: spb; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: tongkang; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: tr_shipment_status; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: tr_shipment_type; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: tugboat; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.users (id, auth_id, username, hashed_password, nama, email, grup, area, opr, cabang, delete_status, add_by, add_time) VALUES ('f507531b-cf76-4a62-9897-c2381fefb3b0', 1, 'sys_admin', 'pbkdf2:sha256:260000$vkFkwQQLgTjrcAGx$57f43846c46278069dae2c0e3b1497fb70361e4d50cf5c8c27ce36a8ba021bfe', 'Admin', NULL, NULL, NULL, NULL, NULL, 0, NULL, '2022-11-07 09:22:52.539152');
INSERT INTO public.users (id, auth_id, username, hashed_password, nama, email, grup, area, opr, cabang, delete_status, add_by, add_time) VALUES ('da0acb58e0e047ac9328edefe607bd80', 2, 'sumatera', 'pbkdf2:sha256:260000$4wRvPzE1esYbHsmr$0b4a24562f864c12b875ec11a686336ecef1b45debc7016e7b56936909b81a87', 'Sumatera', NULL, NULL, NULL, NULL, NULL, 0, 'f507531b-cf76-4a62-9897-c2381fefb3b0', '2022-11-07 09:25:12.170594');
INSERT INTO public.users (id, auth_id, username, hashed_password, nama, email, grup, area, opr, cabang, delete_status, add_by, add_time) VALUES ('b1363ad958c0404f89e6c42e86bbcc4d', 3, 'juliet', 'pbkdf2:sha256:260000$UreItlgigVZDenZf$eaa0d6cf5fa8e66dd73b4a3753a9e942aab81003ae0d4015a9c73dd324b2ea70', 'Juliet', NULL, NULL, NULL, NULL, 'Cilacap', 0, 'f507531b-cf76-4a62-9897-c2381fefb3b0', '2022-11-07 09:26:27.145113');
INSERT INTO public.users (id, auth_id, username, hashed_password, nama, email, grup, area, opr, cabang, delete_status, add_by, add_time) VALUES ('6e5c20a0097242cebd50f661920d6bf0', 4, 'romeo', 'pbkdf2:sha256:260000$3sRE1fxacxqcz81j$87c82c881740c0222fb86bdae71db3a3ef03bd14c03e92ffdb635bebed990156', 'Romeo', NULL, NULL, NULL, 'Adipala', 'Cilacap', 0, 'f507531b-cf76-4a62-9897-c2381fefb3b0', '2022-11-07 09:27:04.39525');


--
-- Data for Name: vessel; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Name: auth_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_id_seq', 4, true);


--
-- Name: jenis_assist_tug_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.jenis_assist_tug_id_seq', 1, false);


--
-- Name: shipment_status_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.shipment_status_id_seq', 1, false);


--
-- Name: shipment_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.shipment_type_id_seq', 1, false);


--
-- Name: agen agen_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.agen
    ADD CONSTRAINT agen_pkey PRIMARY KEY (id);


--
-- Name: assist_tug assist_tug_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.assist_tug
    ADD CONSTRAINT assist_tug_pkey PRIMARY KEY (id);


--
-- Name: auth auth_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth
    ADD CONSTRAINT auth_pkey PRIMARY KEY (id);


--
-- Name: form_anchorage form_anchorage_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.form_anchorage
    ADD CONSTRAINT form_anchorage_pkey PRIMARY KEY (id);


--
-- Name: form_berthed form_berthed_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.form_berthed
    ADD CONSTRAINT form_berthed_pkey PRIMARY KEY (id);


--
-- Name: form_cast_of_jetty form_cast_of_jetty_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.form_cast_of_jetty
    ADD CONSTRAINT form_cast_of_jetty_pkey PRIMARY KEY (id);


--
-- Name: form_onasiling form_onasiling_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.form_onasiling
    ADD CONSTRAINT form_onasiling_pkey PRIMARY KEY (id);


--
-- Name: form_onasiling_tongkang_sts form_onasiling_tongkang_sts_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.form_onasiling_tongkang_sts
    ADD CONSTRAINT form_onasiling_tongkang_sts_pkey PRIMARY KEY (id);


--
-- Name: form_shifting_in form_shifting_in_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.form_shifting_in
    ADD CONSTRAINT form_shifting_in_pkey PRIMARY KEY (id);


--
-- Name: form_shifting_out form_shifting_out_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.form_shifting_out
    ADD CONSTRAINT form_shifting_out_pkey PRIMARY KEY (id);


--
-- Name: jenis_assist_tug jenis_assist_tug_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jenis_assist_tug
    ADD CONSTRAINT jenis_assist_tug_pkey PRIMARY KEY (id);


--
-- Name: pltu pltu_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pltu
    ADD CONSTRAINT pltu_pkey PRIMARY KEY (id);


--
-- Name: shipment_docs shipment_docs_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shipment_docs
    ADD CONSTRAINT shipment_docs_pkey PRIMARY KEY (id);


--
-- Name: shipment shipment_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shipment
    ADD CONSTRAINT shipment_pkey PRIMARY KEY (id);


--
-- Name: shipment_service shipment_service_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shipment_service
    ADD CONSTRAINT shipment_service_pkey PRIMARY KEY (id);


--
-- Name: shipment_status shipment_status_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shipment_status
    ADD CONSTRAINT shipment_status_pkey PRIMARY KEY (id);


--
-- Name: shipment_type shipment_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shipment_type
    ADD CONSTRAINT shipment_type_pkey PRIMARY KEY (id);


--
-- Name: shipper shipper_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shipper
    ADD CONSTRAINT shipper_pkey PRIMARY KEY (id);


--
-- Name: spb spb_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spb
    ADD CONSTRAINT spb_pkey PRIMARY KEY (id);


--
-- Name: tongkang tongkang_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tongkang
    ADD CONSTRAINT tongkang_pkey PRIMARY KEY (id);


--
-- Name: tr_shipment_status tr_shipment_status_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tr_shipment_status
    ADD CONSTRAINT tr_shipment_status_pkey PRIMARY KEY (id);


--
-- Name: tr_shipment_type tr_shipment_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tr_shipment_type
    ADD CONSTRAINT tr_shipment_type_pkey PRIMARY KEY (id);


--
-- Name: tugboat tugboat_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tugboat
    ADD CONSTRAINT tugboat_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: vessel vessel_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vessel
    ADD CONSTRAINT vessel_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

