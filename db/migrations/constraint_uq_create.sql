-- object: account_uk | type: CONSTRAINT --
-- ALTER TABLE public.account DROP CONSTRAINT IF EXISTS account_uk CASCADE;
ALTER TABLE public.account ADD CONSTRAINT account_uk UNIQUE (username);
-- ddl-end --

