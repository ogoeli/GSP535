#import the arcpy env
import arcpy
from arcpy.sa import *
import os
arcpy.env.overwriteOutput = True

#set the working directory to the EX10
arcpy.env.workspace = r'C:\Users\ope4\OneDrive - Northern Arizona University\Desktop\ACADEMIC_SEMSTER\FALL 2026\GSP 535 - PROGRAMMING FOR GIS\WEEK14\Ignore\PythonScripting_Ex10_Data\Ex10'

elevraster = arcpy.Raster("elevation")  #creates a raster object

outraster = elevraster * 3.281 #multiple the object with 3.281. converts the elevation values from meters to feet

outraster.save("elev_ft") #saves the created raster as elev_ft

slope = AspectSlope(elevraster) #creates a raster layer that displays both surface aspect and slope at the same time
goodslope = slope < 20 #if slope is less than 20
goodelev = elevraster < 2500 #if elevation is less than 2500
goodfinal = goodslope & goodelev # logical AND operator, so if both are true
goodfinal.save("final") #saves the created raster as elev_ft
