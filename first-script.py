from osgeo import gdal
from osgeo import osr
import sys

# open dataset

gdal.UseExceptions()

try:
    ds = gdal.Open('images/train_40.tif')
except RuntimeError:
    print("unable to open the tiff file")
    sys.exit(1)

print("\n\n-------metadata---------\n\n")

print(ds.GetMetadata())
band = ds.GetRasterBand(1)
arrayy = band.ReadAsArray()
nodata = band.GetNoDataValue()

print(arrayy)
print(nodata)


print("\n\n-------projectionPrettyWKT---------\n\n")

raster_wkt = ds.GetProjection()
spatial_ref = osr.SpatialReference()
spatial_ref.ImportFromWkt(raster_wkt)
print(spatial_ref.ExportToPrettyWkt())


print("\n\n-------Raster data---------\n\n")

try:
    num_band = ds.RasterCount
except RuntimeError:
    print('band = 1')
    sys.exit(1)


print(num_band)

for i in range(1, num_band):
    band = ds.GetRasterBand(i)
    print(band)  # band 0 might not be printable
    print("\n\n-------GEO INFO data---------\n\n")
    typpe = gdal.GetDataTypeName(band.DataType)
    print("Band Type="+typpe)
    print(ds.RasterXSize)
    print(band.YSize)
    print(ds.GetDriver().LongName)
    print(ds.GetGeoTransform())

    scanline = band.ReadRaster(0, 0, band.XSize, 1, band.XSize, 1, typpe)
    print(scanline)

    print(str(i))

# close dataset
ds = None
