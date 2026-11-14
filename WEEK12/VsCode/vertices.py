#import the arcpy env
import arcpy
arcpy.env.overwriteOutput = True

#set the working directory to the EX09
arcpy.env.workspace = r'C:\Users\ope4\OneDrive - Northern Arizona University\Desktop\ACADEMIC_SEMSTER\FALL 2026\GSP 535 - PROGRAMMING FOR GIS\WEEK12\Ignore\PythonScripting_Ex09_Data\Ex09'

fc = "rivers.shp" #assign the rivers shapefile to fc variable

with arcpy.da.SearchCursor(fc, (["OID@", "SHAPE@"])) as cursor: #use SearchCursor to read data from the feature class created above. this also retrives the OID and shape of each geom and holds it as cursor

    for row in cursor: #a for loop to loop through each feature in the cursor

        print("Feature {0}: ".format(row[0])) #print the feature of the first index

        for point in row[1].getPart(0): #for loop to access the first index [the shape] of each river geometry

            print("{0:.3f}, {1:.3f}".format(point.X, point.Y)) #print the X and Y cord
