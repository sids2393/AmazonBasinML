from osgeo import gdal
from osgeo import osr
import sys

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# show error exceptions on console
gdal.UseExceptions()

try:
    ds = gdal.Open('images/train_40.tif')
except RuntimeError:
    print("unable to open the tiff file")
    sys.exit(1)

print("\n-------metadata---------\n")

print(ds.GetMetadata())

#
#
# I think we don't have the data related to Projections
#
#
# print("\n-------projectionPrettyWKT---------\n")

# raster_wkt = ds.GetProjection()
# spatial_ref = osr.SpatialReference()
# spatial_ref.ImportFromWkt(raster_wkt)
# print(spatial_ref.ExportToPrettyWkt())


print("\n-------Raster data---------\n")

try:
    num_band = ds.RasterCount
except RuntimeError:
    print('band = 1')
    sys.exit(1)


print(num_band)

for i in range(1, num_band):
    band = ds.GetRasterBand(i)
    print(band)  # band 0 might not be printable
    print("\n-------GEO INFO data---------\n")
    typpe = gdal.GetDataTypeName(band.DataType)
    print("Band Type=" + typpe)

    arrayy = band.ReadAsArray()
    nodata = band.GetNoDataValue()

    print(arrayy)  # Data Matrix
    print(nodata)

    print("\n-------X Size---------")
    print(ds.RasterXSize)
    print("\n-------Y size---------")
    print(band.YSize)
    print("\n-------name---------")
    print(ds.GetDriver().LongName)
    print("\n-------colorInterpret---------")
    print(band.GetColorInterpretation())
    print("\n-------Color Table---------")
    print(band.GetRasterColorTable())
    print("\n-------GEO Tranform data---------")
    print(ds.GetGeoTransform())
    print("\n-------get histogram---------")
    print(band.GetDefaultHistogram())
    print("\n-------RasterAttriTable data---------")
    print(band.GetDefaultRAT())

    # scanline = band.ReadRaster(0, 0, band.XSize, 1, band.XSize, 1, typpe)
    # print(scanline)

    # setup Lambert Conformal basemap.
    m = Basemap(width=12000000, height=9000000, projection='lcc',
                resolution='c', lat_1=45., lat_2=55, lat_0=50, lon_0=-107.)
    # draw coastlines.
    m.drawcoastlines()
    # draw a boundary around the map, fill the background.
    # this background will end up being the ocean color, since
    # the continents will be drawn on top.
    m.drawmapboundary(fill_color='aqua')
    # fill continents, set lake color same as ocean color.
    m.fillcontinents(color='coral', lake_color='aqua')
    plt.show()

    print(str(i))

# close dataset
ds = None
