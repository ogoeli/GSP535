#import the arcpy env
import arcpy
arcpy.env.overwriteOutput = True

#set the working directory to the EX09
arcpy.env.workspace = r'C:\Users\ope4\OneDrive - Northern Arizona University\Desktop\ACADEMIC_SEMSTER\FALL 2026\GSP 535 - PROGRAMMING FOR GIS\WEEK12\Ignore\PythonScripting_Ex09_Data\Ex09'

fc = "dams.shp" #assign the dams shapefile to fc variable

with arcpy.da.SearchCursor(fc, (["OID@", "SHAPE@"])) as cursor: #use SearchCursor to read data from the feature class created above. this also retrives the OID and shape of each geom and holds it as cursor

    for row in cursor: #a for loop to loop through each feature in the cursor

        if row[1].isMultipart: #an if else statement to iterate over each fc and print either multipart or single part

            print("Feature {0} is multipart.".format(row[0])) #if the current iteration is multipart, print this else move to the next line

        else: #the else statement of the iteration to check if a fc is a multipart or a single part

            print("Feature {0} is single part.".format(row[0])) #if fc is single part, print this
