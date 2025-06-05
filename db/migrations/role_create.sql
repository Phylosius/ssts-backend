-- object: ssts_app | type: ROLE --
-- DROP ROLE IF EXISTS ssts_app;
CREATE ROLE ssts_app WITH 
	CREATEDB
	LOGIN
	REPLICATION
	 PASSWORD '********';
-- ddl-end --

