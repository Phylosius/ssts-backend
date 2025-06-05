-- object: account_pk | type: CONSTRAINT --
-- ALTER TABLE public.account DROP CONSTRAINT IF EXISTS account_pk CASCADE;
ALTER TABLE public.account ADD CONSTRAINT account_pk PRIMARY KEY (id);
-- ddl-end --

