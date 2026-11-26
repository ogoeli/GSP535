#import the arcpy env
import arcpy
import os
arcpy.env.overwriteOutput = True

#set the working directory to the EX10
arcpy.env.workspace = r'C:\Users\ope4\OneDrive - Northern Arizona University\Desktop\ACADEMIC_SEMSTER\FALL 2026\GSP 535 - PROGRAMMING FOR GIS\WEEK14\Ignore\PythonScripting_Ex10_Data\Ex10'

raster = "tm.img" #the raster image ID

desc = arcpy.da.Describe(raster) #describe the raster, this return a dict object

for rband in desc["children"]: #iterate through each band in the multiband raster

    bandname = rband["baseName"] #assign the current base band to bandname
      
    x = rband["meanCellHeight"] #assign the raster pixel mean cell height and assign the value to x

    y = rband["meanCellWidth"] #assign the raster pixel mean cell width and assign the value to y

    spatialref = desc["spatialReference"] #assign the spatial reference of the raster image

    units = spatialref.linearUnitName #assign the unit of the image, extracted from the spatial refence

    print("The resolution is {0} is {1:.7f} by {2:.7f} {3}." .format(bandname, x, y, units))  # prints the cell size in the units of the coordinate system of the raster
