#import the arcpy env
import arcpy
from arcpy.sa import *
import os
arcpy.env.overwriteOutput = True

#set the working directory to the EX10
arcpy.env.workspace = r'C:\Users\ope4\OneDrive - Northern Arizona University\Desktop\ACADEMIC_SEMSTER\FALL 2026\GSP 535 - PROGRAMMING FOR GIS\WEEK14\Ignore\PythonScripting_Ex10_Data\Ex10'

myremap = RemapRange([[1000,2000,1], [2000,3000,2], [3000,4000,3]]) #define how ranges of input raster values are reclassified and assign it to new output(myremap)

outreclass = Reclassify("elevation", "VALUE", myremap) #reclaiffy the values in the elevation dataset with created myremap

outreclass.save("elev_recl") #save the reclaiffyied output
