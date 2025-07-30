-- object: face_account_fk | type: CONSTRAINT --
-- ALTER TABLE public.face_id DROP CONSTRAINT IF EXISTS face_account_fk CASCADE;
ALTER TABLE public.face_id ADD CONSTRAINT face_account_fk FOREIGN KEY (account_id)
REFERENCES public.account (id) MATCH SIMPLE
ON DELETE CASCADE ON UPDATE NO ACTION;
-- ddl-end --

