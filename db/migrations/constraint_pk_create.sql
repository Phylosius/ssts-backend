-- object: account_pk | type: CONSTRAINT --
-- ALTER TABLE public.account DROP CONSTRAINT IF EXISTS account_pk CASCADE;
ALTER TABLE public.account ADD CONSTRAINT account_pk PRIMARY KEY (id);
-- ddl-end --

-- object: face_id_pk | type: CONSTRAINT --
-- ALTER TABLE public.face_id DROP CONSTRAINT IF EXISTS face_id_pk CASCADE;
ALTER TABLE public.face_id ADD CONSTRAINT face_id_pk PRIMARY KEY (id);
-- ddl-end --

