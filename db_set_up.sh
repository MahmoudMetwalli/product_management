sudo apt update
sudo apt install postgresql postgresql-contrib

sudo -u postgres psql -c "CREATE USER products_admin WITH PASSWORD 'simple#system567';" \
-c "CREATE DATABASE products_db OWNER products_admin;" \
-c "GRANT ALL PRIVILEGES ON DATABASE products_db TO products_admin;"

sudo -u postgres psql -d products_db -c "CREATE EXTENSION pg_trgm;"

sudo -u postgres psql -d products_db -c "GRANT USAGE ON SCHEMA public TO products_admin;"
