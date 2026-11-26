#import the arcpy env
import arcpy
import os
arcpy.env.overwriteOutput = True

#set the working directory to the EX10
arcpy.env.workspace = r'C:\Users\ope4\OneDrive - Northern Arizona University\Desktop\ACADEMIC_SEMSTER\FALL 2026\GSP 535 - PROGRAMMING FOR GIS\WEEK14\Ignore\PythonScripting_Ex10_Data\Ex10'

raster = "landcover.tif" #the raster image ID

desc = arcpy.da.Describe(raster) #describe the raster, this return a dict object

x = desc["meanCellHeight"] #assign the raster pixel mean cell height and assign the value to x

y = desc["meanCellWidth"] #assign the raster pixel mean cell width and assign the value to y

spatialref = desc["spatialReference"] #assign the spatial reference of the raster image

units = spatialref.linearUnitName #assign the unit of the image, extracted from the spatial refence

print("The raster resolution is {0} by {1} {2}.".format(x, y, units)) # prints the cell size in the units of the coordinate system of the raster
