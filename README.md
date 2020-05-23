# Import Ocean Data into Postgres

You can use the data in this repository to create an example reverse geocoder,
as explained in
[the tutorial chapter](https://opencagedata.com/reverse-geocoding/tutorial-building-a-reverse-geocoder) of
[the OpenCage guide to reverse geocoding](https://opencagedata.com/reverse-geocoding).

The repo includes a single GeoJSON file with four ocean shapes.

Load it into Postgres with the following command:
`ogr2ogr -f "PostgreSQL" PG:"dbname=oceans_db user=postgres" "oceans.geojson" -nln oceans`

(Where your database is `oceans_db` and the table is `oceans`)

If you want to append it to existing data, use the `-append` flag

Alternatively, you can load many GeoJSON files in the same directory with the `import-geojson.py` script, passing the directory as a command line parameter.

### Who is OpenCage GmbH?

<a href="https://opencagedata.com"><img src="opencage_logo_300_150.png"></a>

We run the [OpenCage Geocoder](https://opencagedata.com). Learn more [about us](https://opencagedata.com/about). 

We also run [Geomob](https://thegeomob.com), a series of regular meetups for location based service creators, where we do our best to highlight geoinnovation. If you like geo stuff, you will probably enjoy [the Geomob podcast](https://thegeomob.com/podcast/).