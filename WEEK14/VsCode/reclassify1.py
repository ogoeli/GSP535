#import the arcpy env
import arcpy
from arcpy.sa import *
import os
arcpy.env.overwriteOutput = True

#set the working directory to the EX10
arcpy.env.workspace = r'C:\Users\ope4\OneDrive - Northern Arizona University\Desktop\ACADEMIC_SEMSTER\FALL 2026\GSP 535 - PROGRAMMING FOR GIS\WEEK14\Ignore\PythonScripting_Ex10_Data\Ex10'

elevraster = arcpy.Raster("elevation")  #creates a raster object
