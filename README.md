# Import Ocean Data into Postgres

You can use the data in this repository to create an example reverse geocoder. It includes a single GeoJSON file with four ocean shapes.

Load it into Postgres with the following command:
`ogr2ogr -f "PostgreSQL" PG:"dbname=oceans_db user=postgres" "oceans.geojson" -nln oceans`

(Where your database is `oceans_db` and the table is `oceans`)

If you want to append it to existing data, use the `-append` flag

Alternatively, you can load many GeoJSON files in the same directory with the `import-geojson.py` script, passing the directory as a command line parameter.
