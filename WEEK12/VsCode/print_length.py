#import the arcpy env
import arcpy
arcpy.env.overwriteOutput = True

#set the working directory to the EX09
arcpy.env.workspace = r'C:\Users\ope4\OneDrive - Northern Arizona University\Desktop\ACADEMIC_SEMSTER\FALL 2026\GSP 535 - PROGRAMMING FOR GIS\WEEK12\Ignore\PythonScripting_Ex09_Data\Ex09'

fc = "rivers.shp" #assign the rivers shapefile to fc variable

with arcpy.da.SearchCursor(fc, ["SHAPE@LENGTH"]) as cursor: #use SearchCursor to read data from the feature class created above. this also retrives the length of each geom and holds it as cursor

    length = 0 #creates a variable and assigns the intial value to 0

    for row in cursor: #a for loop to loop through each feature in the cursor
        length = length + row[0] # and add the each length to the cumulative lenght variable

    #print(length) #print out the value of the length stored

    desc = arcpy.da.Describe(fc) #describes the fc and result stored in desc

    units = desc["spatialReference"].linearUnitName #access the unit from the fc description

    print(f"{length:.2f} {units}") #prints the length and unit
