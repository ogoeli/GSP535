#The script creates a search cursor on the feature class and uses a for loop to iterate 
#over all the rows of the attribute table.

#import the arcpy env
import arcpy
arcpy.env.overwriteOutput = True

#set the working directory to the EX08
arcpy.env.workspace = r'C:\Users\ope4\OneDrive - Northern Arizona University\Desktop\ACADEMIC_SEMSTER\FALL 2026\GSP 535 - PROGRAMMING FOR GIS\WEEK11\Ignore\PythonScripting_Ex08_Data\Ex08'


fc = "airports.shp" #this assigns the shapefile data in the GDB to a variable named fc

cursor = arcpy.da.SearchCursor(fc, ["NAME"]) # the following calls the SearchCursor class to create a cursor

for row in cursor: # loop through rows in the cursor created above
    print("Airport name = {0}".format(row[0])) # print the row data starting from index 0
