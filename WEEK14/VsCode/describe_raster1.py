#import the arcpy env
import arcpy
import fileinput 
import os
arcpy.env.overwriteOutput = True

#set the working directory to the EX10
arcpy.env.workspace = r'C:\Users\ope4\OneDrive - Northern Arizona University\Desktop\ACADEMIC_SEMSTER\FALL 2026\GSP 535 - PROGRAMMING FOR GIS\WEEK14\Ignore\PythonScripting_Ex10_Data\Ex10'

raster = "landcover.tif" #the raster image ID

desc = arcpy.da.Describe(raster) #describe the raster, this return a dict object

print("Raster base name: " + desc["baseName"]) #from the dict, print the raster base name

print("Raster data type: " + desc["dataType"]) #from the dict, print the raster datatype

print("Raster file extension: " + desc["extension"]) #from the dict, print the file extension

print("Raster base name: {0}".format(desc["baseName"])) #prin the base name using format

print("Raster spatial reference: " + desc["spatialReference"].name) #from the dict, print the raster spatial reference

print("Raster format: " + desc["format"]) #from the dict, print the raster format

print("Raster compression: " + desc["compressionType"]) #from the dict, print the raster compression type

print("Raster number of bands: " + str(desc["bandCount"])) #from the dict, print the raster band count


