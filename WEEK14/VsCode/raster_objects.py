#import the arcpy env
import arcpy
import os
arcpy.env.overwriteOutput = True

#set the working directory to the EX10
arcpy.env.workspace = r'C:\Users\ope4\OneDrive - Northern Arizona University\Desktop\ACADEMIC_SEMSTER\FALL 2026\GSP 535 - PROGRAMMING FOR GIS\WEEK14\Ignore\PythonScripting_Ex10_Data\Ex10'

outraster = arcpy.sa.Slope("elevation") #decribe the slope of the the raster

#desc = arcpy.da.Describe(outraster) #describe the object created above, output is a dict

#print(desc["datasetType"]) #print the dataset type

#print(desc["permanent"]) #determine the permanent state of the raster.

outraster.save("slope") # save() method can be used to make the raster permanent, the commented out lines creates a temp slope raster
