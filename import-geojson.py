#!/usr/bin/env python
# coding: utf-8

import os

create_table = True

for i in os.listdir(os.getcwd()):
    if i.lower().endswith(('.geojson')):
        if create_table == True:
            os.system(f'ogr2ogr -f "PostgreSQL" PG:"dbname=oceans_db user=postgres" "{i}" -nln oceans')
            create_table = False
        else:
            os.system(f'ogr2ogr -f "PostgreSQL" PG:"dbname=oceans_db user=postgres" "{i}" -nln oceans -append')

