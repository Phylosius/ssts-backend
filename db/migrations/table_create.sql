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

-- object: public.face_id | type: TABLE --
-- DROP TABLE IF EXISTS public.face_id CASCADE;
CREATE TABLE public.face_id (
	id varchar NOT NULL,
	account_id varchar NOT NULL,
	added_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
	face_encodings float8[] NOT NULL

);
-- ddl-end --
ALTER TABLE public.face_id OWNER TO ssts_app;
-- ddl-end --

