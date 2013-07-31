tulsa_hydrants
==============

Basic scripts for moving around hydrant data

api_csv_.py  -- downloads hydrants from the oklahoma boundary service and saves as a csv.

The resulting file was put into TileMill and uploaded to Mapbox. 

Results are at: http://a.tiles.mapbox.com/v3/jdungan.TFDD.html

csv_geojson converts csv to geojson -- very simple, very hardcoded, you even have to remove the last comma

but... it works.  check out the hydrants.geojson file automajically displayed by Mapbox.
