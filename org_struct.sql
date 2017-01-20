--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: new_records; Type: TABLE; Schema: public; Owner: priyanshi; Tablespace: 
--

CREATE TABLE new_records (
    parent_team_id integer,
    child_team_id integer,
    sub_chil_id integer
);


ALTER TABLE new_records OWNER TO priyanshi;

--
-- Name: org_mapping; Type: TABLE; Schema: public; Owner: priyanshi; Tablespace: 
--

CREATE TABLE org_mapping (
    org_id integer,
    org_name text
);


ALTER TABLE org_mapping OWNER TO priyanshi;

--
-- Name: org_team; Type: TABLE; Schema: public; Owner: priyanshi; Tablespace: 
--

CREATE TABLE org_team (
    org_id integer,
    team_id integer
);


ALTER TABLE org_team OWNER TO priyanshi;

--
-- Name: password; Type: TABLE; Schema: public; Owner: priyanshi; Tablespace: 
--

CREATE TABLE password (
    userid integer,
    salt text,
    hashedpass text
);


ALTER TABLE password OWNER TO priyanshi;

--
-- Name: repo_mapping; Type: TABLE; Schema: public; Owner: priyanshi; Tablespace: 
--

CREATE TABLE repo_mapping (
    repo_id integer,
    repo_name text
);


ALTER TABLE repo_mapping OWNER TO priyanshi;

--
-- Name: session; Type: TABLE; Schema: public; Owner: priyanshi; Tablespace: 
--

CREATE TABLE session (
    sessionuserid text,
    sessionid text NOT NULL,
    ipaddress text,
    expiry timestamp without time zone
);


ALTER TABLE session OWNER TO priyanshi;

--
-- Name: team_mapping; Type: TABLE; Schema: public; Owner: priyanshi; Tablespace: 
--

CREATE TABLE team_mapping (
    team_id integer,
    team_name text
);


ALTER TABLE team_mapping OWNER TO priyanshi;

--
-- Name: team_repo; Type: TABLE; Schema: public; Owner: priyanshi; Tablespace: 
--

CREATE TABLE team_repo (
    team_id integer,
    repo_id integer
);


ALTER TABLE team_repo OWNER TO priyanshi;

--
-- Name: team_under_team; Type: TABLE; Schema: public; Owner: priyanshi; Tablespace: 
--

CREATE TABLE team_under_team (
    parent_team_id integer,
    child_team_id integer
);


ALTER TABLE team_under_team OWNER TO priyanshi;

--
-- Name: users; Type: TABLE; Schema: public; Owner: priyanshi; Tablespace: 
--

CREATE TABLE users (
    userid bigint NOT NULL,
    username text,
    firstname text,
    lastname text,
    role integer,
    repoids integer[],
    teamids integer[]
);


ALTER TABLE users OWNER TO priyanshi;

--
-- Name: users_userid_seq; Type: SEQUENCE; Schema: public; Owner: priyanshi
--

CREATE SEQUENCE users_userid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE users_userid_seq OWNER TO priyanshi;

--
-- Name: users_userid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: priyanshi
--

ALTER SEQUENCE users_userid_seq OWNED BY users.userid;


--
-- Name: userid; Type: DEFAULT; Schema: public; Owner: priyanshi
--

ALTER TABLE ONLY users ALTER COLUMN userid SET DEFAULT nextval('users_userid_seq'::regclass);


--
-- Data for Name: new_records; Type: TABLE DATA; Schema: public; Owner: priyanshi
--

COPY new_records (parent_team_id, child_team_id, sub_chil_id) FROM stdin;
5	6	7
\.


--
-- Data for Name: org_mapping; Type: TABLE DATA; Schema: public; Owner: priyanshi
--

COPY org_mapping (org_id, org_name) FROM stdin;
\.


--
-- Data for Name: org_team; Type: TABLE DATA; Schema: public; Owner: priyanshi
--

COPY org_team (org_id, team_id) FROM stdin;
1	1
1	5
2	8
2	9
2	10
\.


--
-- Data for Name: password; Type: TABLE DATA; Schema: public; Owner: priyanshi
--

COPY password (userid, salt, hashedpass) FROM stdin;
\.


--
-- Data for Name: repo_mapping; Type: TABLE DATA; Schema: public; Owner: priyanshi
--

COPY repo_mapping (repo_id, repo_name) FROM stdin;
\.


--
-- Data for Name: session; Type: TABLE DATA; Schema: public; Owner: priyanshi
--

COPY session (sessionuserid, sessionid, ipaddress, expiry) FROM stdin;
\.


--
-- Data for Name: team_mapping; Type: TABLE DATA; Schema: public; Owner: priyanshi
--

COPY team_mapping (team_id, team_name) FROM stdin;
\.


--
-- Data for Name: team_repo; Type: TABLE DATA; Schema: public; Owner: priyanshi
--

COPY team_repo (team_id, repo_id) FROM stdin;
2	1
3	2
3	11
1	3
5	4
6	5
7	6
6	12
6	7
10	8
8	9
9	10
9	13
\.


--
-- Data for Name: team_under_team; Type: TABLE DATA; Schema: public; Owner: priyanshi
--

COPY team_under_team (parent_team_id, child_team_id) FROM stdin;
1	2
1	3
1	4
5	6
8	10
6	7
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: priyanshi
--

COPY users (userid, username, firstname, lastname, role, repoids, teamids) FROM stdin;
1	Priyanshi.Khatri	Priyanshi	Khatri	1	{1,2,11,9}	{10}
\.


--
-- Name: users_userid_seq; Type: SEQUENCE SET; Schema: public; Owner: priyanshi
--

SELECT pg_catalog.setval('users_userid_seq', 1, true);


--
-- Name: session_pkey; Type: CONSTRAINT; Schema: public; Owner: priyanshi; Tablespace: 
--

ALTER TABLE ONLY session
    ADD CONSTRAINT session_pkey PRIMARY KEY (sessionid);


--
-- Name: users_pkey; Type: CONSTRAINT; Schema: public; Owner: priyanshi; Tablespace: 
--

ALTER TABLE ONLY users
    ADD CONSTRAINT users_pkey PRIMARY KEY (userid);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

