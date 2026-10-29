#this script imports the arcpy env, sets the workspace,
#processes the 'fieldlist' variable and runs a
#for loop that loops every field property in the list,
#the scprit prints the name of the field and the data type

#import the arcpy env
import arcpy
arcpy.env.overwriteOutput = True

#set the working directory to the EX06
arcpy.env.workspace = r'C:\Users\ope4\OneDrive - Northern Arizona University\Desktop\ACADEMIC_SEMSTER\FALL 2026\GSP 535 - PROGRAMMING FOR GIS\WEEK10\Ignore\PythonScripting_Ex06_Data\Ex06'

fieldlist = arcpy.ListFields("cities.shp") # call ListFields() returns a list of Field objects from the 'cities.shp' shapefile

for field in fieldlist: #start of the for loop
    print(field.name + " " + field.type) #print statement
