-- object: public.account | type: TABLE --
-- DROP TABLE IF EXISTS public.account CASCADE;
CREATE TABLE public.account (
	id varchar NOT NULL,
	username varchar NOT NULL,
	email varchar NOT NULL,
	password varchar NOT NULL

);
-- ddl-end --
ALTER TABLE public.account OWNER TO ssts_app;
-- ddl-end --

