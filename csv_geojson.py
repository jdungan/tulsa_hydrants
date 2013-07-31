import csv
 
# Read in raw data from csv
rawData = csv.reader(open('hydrants.csv', 'rb'), dialect='excel')
 
# the template. where data from the csv will be formatted to geojson
template = \
    ''' \
    { "type" : "Feature",
        "id" : %s,
            "geometry" : {
                "type" : "Point",
                "coordinates" : ["%s","%s"]},
        "properties" : { "name" : "%s", "value" : "%s"}
        },
    '''
 
# the head of the geojson file
output = \
    ''' \
{ "type" : "Feature Collection",
    {"features" : [
    '''
 
#  lat 30
#  lng 18
 
# loop through the csv by row skipping the first
iter = 0
for row in rawData:
    iter += 1
    if iter >= 2:
        id = row[17]
        lat = row[30]
        lng = row[18]
        name = row[29]
        pop = row[2]
        output += template % (id, lat, lng, name, pop)
 
# the tail of the geojson file
output += \
    ''' \
    ]
}
    '''
 
# opens an geoJSON file to write the output to
outFileHandle = open("hydrants.geojson", "w")
outFileHandle.write(output)
outFileHandle.close()
