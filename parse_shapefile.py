import shapefile

sf = shapefile.Reader('airports.shp')
print('READER Object: %s' % sf)

shapes = sf.shapes()
print('ROWS: %s' % len(shapes))

for shape in list(sf.iterShapes())[:3]:
    print(shape.shapeType)
