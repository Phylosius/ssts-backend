CREATE USER ssts_db_user WITH PASSWORD 'ssts manager password';
CREATE DATABASE ssts_db OWNER ssts_db_user;
GRANT ALL PRIVILEGES ON DATABASE ssts_db TO ssts_db_user;

