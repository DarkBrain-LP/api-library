--
-- PostgreSQL database dump
--

-- Dumped from database version 12.9 (Ubuntu 12.9-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.9 (Ubuntu 12.9-0ubuntu0.20.04.1)

-- Started on 2022-02-14 12:46:53 GMT

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 203 (class 1259 OID 16498)
-- Name: categories; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.categories (
    id_cat integer NOT NULL,
    libelle character varying(50) NOT NULL
);


ALTER TABLE public.categories OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 16496)
-- Name: categories_id_cat_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.categories_id_cat_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.categories_id_cat_seq OWNER TO postgres;

--
-- TOC entry 2980 (class 0 OID 0)
-- Dependencies: 202
-- Name: categories_id_cat_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.categories_id_cat_seq OWNED BY public.categories.id_cat;


--
-- TOC entry 205 (class 1259 OID 16506)
-- Name: livres; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.livres (
    id integer NOT NULL,
    isbn character varying(30),
    titre character varying(100) NOT NULL,
    date date NOT NULL,
    auteur character varying(100) NOT NULL,
    editeur character varying(100),
    id_cat integer NOT NULL
);


ALTER TABLE public.livres OWNER TO postgres;

--
-- TOC entry 204 (class 1259 OID 16504)
-- Name: livres_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.livres_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.livres_id_seq OWNER TO postgres;

--
-- TOC entry 2981 (class 0 OID 0)
-- Dependencies: 204
-- Name: livres_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.livres_id_seq OWNED BY public.livres.id;


--
-- TOC entry 2836 (class 2604 OID 16501)
-- Name: categories id_cat; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categories ALTER COLUMN id_cat SET DEFAULT nextval('public.categories_id_cat_seq'::regclass);


--
-- TOC entry 2837 (class 2604 OID 16509)
-- Name: livres id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livres ALTER COLUMN id SET DEFAULT nextval('public.livres_id_seq'::regclass);


--
-- TOC entry 2972 (class 0 OID 16498)
-- Dependencies: 203
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.categories (id_cat, libelle) FROM stdin;
4	Romanciere
5	Scientifique
6	Psychologique
7	Médécine
8	Informatique
9	Business
11	Football
2	Animale
1	Litterature
12	Gastronomie
\.


--
-- TOC entry 2974 (class 0 OID 16506)
-- Dependencies: 205
-- Data for Name: livres; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.livres (id, isbn, titre, date, auteur, editeur, id_cat) FROM stdin;
3	123-10-1	Une merveilleuse histoire du temps	2019-05-05	Stephen hawking	Philippe Goutiers	7
4	010-11-10	100 Raisons de vivre	2022-10-10	Le Phoulosophe	Espoir LeCharpentier	11
6	978-0-321	The art of computer programming	2020-03-26	Donald Knuth	Addenda	11
1	978-3-16	Hands on machine learning with scikit learn-Update	2017-10-12	Jean Dupond	Jean DuBridge	8
\.


--
-- TOC entry 2982 (class 0 OID 0)
-- Dependencies: 202
-- Name: categories_id_cat_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.categories_id_cat_seq', 12, true);


--
-- TOC entry 2983 (class 0 OID 0)
-- Dependencies: 204
-- Name: livres_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.livres_id_seq', 6, true);


--
-- TOC entry 2839 (class 2606 OID 16503)
-- Name: categories categories_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (id_cat);


--
-- TOC entry 2841 (class 2606 OID 16520)
-- Name: livres livres_isbn_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livres
    ADD CONSTRAINT livres_isbn_key UNIQUE (isbn);


--
-- TOC entry 2843 (class 2606 OID 16511)
-- Name: livres livres_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livres
    ADD CONSTRAINT livres_pkey PRIMARY KEY (id);


--
-- TOC entry 2844 (class 2606 OID 16514)
-- Name: livres livres_id_cat_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livres
    ADD CONSTRAINT livres_id_cat_fkey FOREIGN KEY (id_cat) REFERENCES public.categories(id_cat);


-- Completed on 2022-02-14 12:46:54 GMT

--
-- PostgreSQL database dump complete
--

