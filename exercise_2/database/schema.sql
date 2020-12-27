--
-- PostgreSQL database dump
--

-- Dumped from database version 12.5 (Ubuntu 12.5-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.5 (Ubuntu 12.5-0ubuntu0.20.04.1)

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

ALTER TABLE IF EXISTS ONLY public.scientist_works_at_faculty DROP CONSTRAINT IF EXISTS scientist_works_at_faculty_scientist_scientist_id_fk;
ALTER TABLE IF EXISTS ONLY public.scientist_works_at_faculty DROP CONSTRAINT IF EXISTS scientist_works_at_faculty_faculty_faculty_id_fk;
ALTER TABLE IF EXISTS ONLY public.scientist_participates_at_conference DROP CONSTRAINT IF EXISTS scientist_participates_at_conference_scientist_scientist_id_fk;
ALTER TABLE IF EXISTS ONLY public.scientist_participates_at_conference DROP CONSTRAINT IF EXISTS scientist_participates_at_conference_conference_conference_id_f;
ALTER TABLE IF EXISTS ONLY public.publication_secondary_author DROP CONSTRAINT IF EXISTS publication_secondary_author_scientist_scientist_id_fk;
ALTER TABLE IF EXISTS ONLY public.publication_secondary_author DROP CONSTRAINT IF EXISTS publication_secondary_author_publication_publication_id_fk;
ALTER TABLE IF EXISTS ONLY public.publication DROP CONSTRAINT IF EXISTS publication_scientist_scientist_id_fk;
ALTER TABLE IF EXISTS ONLY public.publication DROP CONSTRAINT IF EXISTS publication_funding_funding_id_fk;
ALTER TABLE IF EXISTS ONLY public.publication DROP CONSTRAINT IF EXISTS publication_conference_conference_id_fk;
ALTER TABLE IF EXISTS ONLY public.phd DROP CONSTRAINT IF EXISTS phd_scientist_scientist_id_fk_2;
ALTER TABLE IF EXISTS ONLY public.phd DROP CONSTRAINT IF EXISTS phd_scientist_scientist_id_fk;
ALTER TABLE IF EXISTS ONLY public.funding DROP CONSTRAINT IF EXISTS funding_scientist_scientist_id_fk;
ALTER TABLE IF EXISTS ONLY public.funding_funds_phd DROP CONSTRAINT IF EXISTS funding_funds_phd_phd_phd_id_fk;
ALTER TABLE IF EXISTS ONLY public.funding_funds_phd DROP CONSTRAINT IF EXISTS funding_funds_phd_funding_funding_id_fk;
ALTER TABLE IF EXISTS ONLY public.conference DROP CONSTRAINT IF EXISTS conference_faculty_faculty_id_fk;
ALTER TABLE IF EXISTS ONLY public.conference DROP CONSTRAINT IF EXISTS conference_address_address_id_fk;
DROP INDEX IF EXISTS public.publication_publication_id_uindex;
DROP INDEX IF EXISTS public.phd_phd_id_uindex;
DROP INDEX IF EXISTS public.funding_funding_id_uindex;
DROP INDEX IF EXISTS public.conference_conference_id_uindex;
ALTER TABLE IF EXISTS ONLY public.scientist_works_at_faculty DROP CONSTRAINT IF EXISTS scientist_works_at_faculty_pk;
ALTER TABLE IF EXISTS ONLY public.scientist DROP CONSTRAINT IF EXISTS scientist_pk;
ALTER TABLE IF EXISTS ONLY public.scientist_participates_at_conference DROP CONSTRAINT IF EXISTS scientist_participates_at_conference_pk;
ALTER TABLE IF EXISTS ONLY public.publication_secondary_author DROP CONSTRAINT IF EXISTS publication_secondary_author_pk;
ALTER TABLE IF EXISTS ONLY public.publication DROP CONSTRAINT IF EXISTS publication_pk;
ALTER TABLE IF EXISTS ONLY public.phd DROP CONSTRAINT IF EXISTS phd_pk;
ALTER TABLE IF EXISTS ONLY public.funding DROP CONSTRAINT IF EXISTS funding_pk;
ALTER TABLE IF EXISTS ONLY public.funding_funds_phd DROP CONSTRAINT IF EXISTS funding_funds_phd_pk;
ALTER TABLE IF EXISTS ONLY public.faculty DROP CONSTRAINT IF EXISTS faculty_pk;
ALTER TABLE IF EXISTS ONLY public.conference DROP CONSTRAINT IF EXISTS conference_pk;
ALTER TABLE IF EXISTS ONLY public.address DROP CONSTRAINT IF EXISTS address_pk;
ALTER TABLE IF EXISTS public.scientist ALTER COLUMN scientist_id DROP DEFAULT;
ALTER TABLE IF EXISTS public.publication ALTER COLUMN publication_id DROP DEFAULT;
ALTER TABLE IF EXISTS public.phd ALTER COLUMN phd_id DROP DEFAULT;
ALTER TABLE IF EXISTS public.funding ALTER COLUMN funding_id DROP DEFAULT;
ALTER TABLE IF EXISTS public.faculty ALTER COLUMN faculty_id DROP DEFAULT;
ALTER TABLE IF EXISTS public.conference ALTER COLUMN conference_id DROP DEFAULT;
ALTER TABLE IF EXISTS public.address ALTER COLUMN address_id DROP DEFAULT;
DROP TABLE IF EXISTS public.scientist_works_at_faculty;
DROP SEQUENCE IF EXISTS public.scientist_scientist_id_seq;
DROP TABLE IF EXISTS public.scientist_participates_at_conference;
DROP TABLE IF EXISTS public.scientist;
DROP TABLE IF EXISTS public.publication_secondary_author;
DROP SEQUENCE IF EXISTS public.publication_publication_id_seq;
DROP TABLE IF EXISTS public.publication;
DROP SEQUENCE IF EXISTS public.phd_phd_id_seq;
DROP TABLE IF EXISTS public.phd;
DROP TABLE IF EXISTS public.funding_funds_phd;
DROP SEQUENCE IF EXISTS public.funding_funding_id_seq;
DROP TABLE IF EXISTS public.funding;
DROP SEQUENCE IF EXISTS public.faculty_faculty_id_seq;
DROP TABLE IF EXISTS public.faculty;
DROP SEQUENCE IF EXISTS public.conference_conference_id_seq;
DROP TABLE IF EXISTS public.conference;
DROP SEQUENCE IF EXISTS public."2016_address_address_id_seq";
DROP TABLE IF EXISTS public.address;
SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: address; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.address (
    address_id bigint NOT NULL,
    address_name character varying NOT NULL,
    address_number character varying NOT NULL,
    city character varying NOT NULL,
    country character varying NOT NULL,
    postal_code character varying NOT NULL
);


--
-- Name: 2016_address_address_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public."2016_address_address_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: 2016_address_address_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public."2016_address_address_id_seq" OWNED BY public.address.address_id;


--
-- Name: conference; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.conference (
    conference_id bigint NOT NULL,
    faculty_id bigint NOT NULL,
    address_id bigint NOT NULL,
    start_date date NOT NULL,
    end_date date NOT NULL,
    title character varying NOT NULL,
    fee numeric(6,2) NOT NULL
);


--
-- Name: conference_conference_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.conference_conference_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: conference_conference_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.conference_conference_id_seq OWNED BY public.conference.conference_id;


--
-- Name: faculty; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.faculty (
    faculty_id bigint NOT NULL,
    name character varying NOT NULL,
    university_name character varying NOT NULL
);


--
-- Name: faculty_faculty_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.faculty_faculty_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: faculty_faculty_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.faculty_faculty_id_seq OWNED BY public.faculty.faculty_id;


--
-- Name: funding; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.funding (
    funding_id bigint NOT NULL,
    scientist_id bigint NOT NULL,
    funder character varying NOT NULL,
    budget numeric(10,2) NOT NULL,
    start_date date NOT NULL,
    end_date date NOT NULL
);


--
-- Name: funding_funding_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.funding_funding_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: funding_funding_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.funding_funding_id_seq OWNED BY public.funding.funding_id;


--
-- Name: funding_funds_phd; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.funding_funds_phd (
    funding_id bigint NOT NULL,
    phd_id bigint NOT NULL,
    working_hours_spent numeric(9,1) NOT NULL
);


--
-- Name: phd; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.phd (
    phd_id bigint NOT NULL,
    date_received date NOT NULL,
    description text NOT NULL,
    supervisor_id bigint NOT NULL,
    title character varying NOT NULL,
    scientist_id bigint NOT NULL
);


--
-- Name: phd_phd_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.phd_phd_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: phd_phd_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.phd_phd_id_seq OWNED BY public.phd.phd_id;


--
-- Name: publication; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.publication (
    publication_id bigint NOT NULL,
    main_author_id bigint NOT NULL,
    title character varying NOT NULL,
    summary text NOT NULL,
    conference_id bigint NOT NULL,
    funding_id bigint NOT NULL,
    won_first_prize boolean DEFAULT false NOT NULL
);


--
-- Name: publication_publication_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.publication_publication_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: publication_publication_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.publication_publication_id_seq OWNED BY public.publication.publication_id;


--
-- Name: publication_secondary_author; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.publication_secondary_author (
    author_id bigint NOT NULL,
    publication_id bigint NOT NULL
);


--
-- Name: scientist; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.scientist (
    scientist_id bigint NOT NULL,
    title character varying NOT NULL,
    name character varying NOT NULL,
    surname character varying NOT NULL
);


--
-- Name: scientist_participates_at_conference; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.scientist_participates_at_conference (
    conference_id bigint NOT NULL,
    scientist_id bigint NOT NULL,
    is_volunteer boolean DEFAULT false NOT NULL
);


--
-- Name: scientist_scientist_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.scientist_scientist_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: scientist_scientist_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.scientist_scientist_id_seq OWNED BY public.scientist.scientist_id;


--
-- Name: scientist_works_at_faculty; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.scientist_works_at_faculty (
    faculty_id bigint NOT NULL,
    scientist_id bigint NOT NULL
);


--
-- Name: address address_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.address ALTER COLUMN address_id SET DEFAULT nextval('public."2016_address_address_id_seq"'::regclass);


--
-- Name: conference conference_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.conference ALTER COLUMN conference_id SET DEFAULT nextval('public.conference_conference_id_seq'::regclass);


--
-- Name: faculty faculty_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.faculty ALTER COLUMN faculty_id SET DEFAULT nextval('public.faculty_faculty_id_seq'::regclass);


--
-- Name: funding funding_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.funding ALTER COLUMN funding_id SET DEFAULT nextval('public.funding_funding_id_seq'::regclass);


--
-- Name: phd phd_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.phd ALTER COLUMN phd_id SET DEFAULT nextval('public.phd_phd_id_seq'::regclass);


--
-- Name: publication publication_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.publication ALTER COLUMN publication_id SET DEFAULT nextval('public.publication_publication_id_seq'::regclass);


--
-- Name: scientist scientist_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.scientist ALTER COLUMN scientist_id SET DEFAULT nextval('public.scientist_scientist_id_seq'::regclass);


--
-- Name: address address_pk; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.address
    ADD CONSTRAINT address_pk PRIMARY KEY (address_id);


--
-- Name: conference conference_pk; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.conference
    ADD CONSTRAINT conference_pk PRIMARY KEY (conference_id, faculty_id);


--
-- Name: faculty faculty_pk; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.faculty
    ADD CONSTRAINT faculty_pk PRIMARY KEY (faculty_id);


--
-- Name: funding_funds_phd funding_funds_phd_pk; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.funding_funds_phd
    ADD CONSTRAINT funding_funds_phd_pk PRIMARY KEY (funding_id, phd_id);


--
-- Name: funding funding_pk; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.funding
    ADD CONSTRAINT funding_pk PRIMARY KEY (funding_id, scientist_id);


--
-- Name: phd phd_pk; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.phd
    ADD CONSTRAINT phd_pk PRIMARY KEY (phd_id, scientist_id);


--
-- Name: publication publication_pk; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.publication
    ADD CONSTRAINT publication_pk PRIMARY KEY (publication_id, main_author_id);


--
-- Name: publication_secondary_author publication_secondary_author_pk; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.publication_secondary_author
    ADD CONSTRAINT publication_secondary_author_pk PRIMARY KEY (author_id, publication_id);


--
-- Name: scientist_participates_at_conference scientist_participates_at_conference_pk; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.scientist_participates_at_conference
    ADD CONSTRAINT scientist_participates_at_conference_pk PRIMARY KEY (conference_id, scientist_id);


--
-- Name: scientist scientist_pk; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.scientist
    ADD CONSTRAINT scientist_pk PRIMARY KEY (scientist_id);


--
-- Name: scientist_works_at_faculty scientist_works_at_faculty_pk; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.scientist_works_at_faculty
    ADD CONSTRAINT scientist_works_at_faculty_pk PRIMARY KEY (faculty_id, scientist_id);


--
-- Name: conference_conference_id_uindex; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX conference_conference_id_uindex ON public.conference USING btree (conference_id);


--
-- Name: funding_funding_id_uindex; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX funding_funding_id_uindex ON public.funding USING btree (funding_id);


--
-- Name: phd_phd_id_uindex; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX phd_phd_id_uindex ON public.phd USING btree (phd_id);


--
-- Name: publication_publication_id_uindex; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX publication_publication_id_uindex ON public.publication USING btree (publication_id);


--
-- Name: conference conference_address_address_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.conference
    ADD CONSTRAINT conference_address_address_id_fk FOREIGN KEY (address_id) REFERENCES public.address(address_id);


--
-- Name: conference conference_faculty_faculty_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.conference
    ADD CONSTRAINT conference_faculty_faculty_id_fk FOREIGN KEY (faculty_id) REFERENCES public.faculty(faculty_id);


--
-- Name: funding_funds_phd funding_funds_phd_funding_funding_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.funding_funds_phd
    ADD CONSTRAINT funding_funds_phd_funding_funding_id_fk FOREIGN KEY (funding_id) REFERENCES public.funding(funding_id);


--
-- Name: funding_funds_phd funding_funds_phd_phd_phd_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.funding_funds_phd
    ADD CONSTRAINT funding_funds_phd_phd_phd_id_fk FOREIGN KEY (phd_id) REFERENCES public.phd(phd_id);


--
-- Name: funding funding_scientist_scientist_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.funding
    ADD CONSTRAINT funding_scientist_scientist_id_fk FOREIGN KEY (scientist_id) REFERENCES public.scientist(scientist_id);


--
-- Name: phd phd_scientist_scientist_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.phd
    ADD CONSTRAINT phd_scientist_scientist_id_fk FOREIGN KEY (scientist_id) REFERENCES public.scientist(scientist_id);


--
-- Name: phd phd_scientist_scientist_id_fk_2; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.phd
    ADD CONSTRAINT phd_scientist_scientist_id_fk_2 FOREIGN KEY (supervisor_id) REFERENCES public.scientist(scientist_id);


--
-- Name: publication publication_conference_conference_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.publication
    ADD CONSTRAINT publication_conference_conference_id_fk FOREIGN KEY (conference_id) REFERENCES public.conference(conference_id);


--
-- Name: publication publication_funding_funding_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.publication
    ADD CONSTRAINT publication_funding_funding_id_fk FOREIGN KEY (funding_id) REFERENCES public.funding(funding_id);


--
-- Name: publication publication_scientist_scientist_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.publication
    ADD CONSTRAINT publication_scientist_scientist_id_fk FOREIGN KEY (main_author_id) REFERENCES public.scientist(scientist_id);


--
-- Name: publication_secondary_author publication_secondary_author_publication_publication_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.publication_secondary_author
    ADD CONSTRAINT publication_secondary_author_publication_publication_id_fk FOREIGN KEY (publication_id) REFERENCES public.publication(publication_id);


--
-- Name: publication_secondary_author publication_secondary_author_scientist_scientist_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.publication_secondary_author
    ADD CONSTRAINT publication_secondary_author_scientist_scientist_id_fk FOREIGN KEY (author_id) REFERENCES public.scientist(scientist_id);


--
-- Name: scientist_participates_at_conference scientist_participates_at_conference_conference_conference_id_f; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.scientist_participates_at_conference
    ADD CONSTRAINT scientist_participates_at_conference_conference_conference_id_f FOREIGN KEY (conference_id) REFERENCES public.conference(conference_id);


--
-- Name: scientist_participates_at_conference scientist_participates_at_conference_scientist_scientist_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.scientist_participates_at_conference
    ADD CONSTRAINT scientist_participates_at_conference_scientist_scientist_id_fk FOREIGN KEY (scientist_id) REFERENCES public.scientist(scientist_id);


--
-- Name: scientist_works_at_faculty scientist_works_at_faculty_faculty_faculty_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.scientist_works_at_faculty
    ADD CONSTRAINT scientist_works_at_faculty_faculty_faculty_id_fk FOREIGN KEY (faculty_id) REFERENCES public.faculty(faculty_id);


--
-- Name: scientist_works_at_faculty scientist_works_at_faculty_scientist_scientist_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.scientist_works_at_faculty
    ADD CONSTRAINT scientist_works_at_faculty_scientist_scientist_id_fk FOREIGN KEY (scientist_id) REFERENCES public.scientist(scientist_id);


--
-- PostgreSQL database dump complete
--

