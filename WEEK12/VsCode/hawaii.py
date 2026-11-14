#import the arcpy env
import arcpy
arcpy.env.overwriteOutput = True

#set the working directory to the EX09
arcpy.env.workspace = r'C:\Users\ope4\OneDrive - Northern Arizona University\Desktop\ACADEMIC_SEMSTER\FALL 2026\GSP 535 - PROGRAMMING FOR GIS\WEEK12\Ignore\PythonScripting_Ex09_Data\Ex09'

fc = "hawaii.shp" #assign the dams shapefile to fc variable

with arcpy.da.SearchCursor(fc, (["OID@", "SHAPE@"])) as cursor: #use SearchCursor to read data from the feature class created above. this also retrives the OID and shape of each geom and holds it as cursor

    for row in cursor: #a for loop to loop through each feature in the cursor

        print("Feature {0}: ".format(row[0])) #print this index 0 content
        
        partnum = 0 #create an variable and assign its intial vaule to 0

        for part in row[1]: #for each part in the shape geom 

            print("Part {0}: ".format(partnum)) #print the part number

            for point in part: #loop through each point in the part and for each point in that part

                print("{0:.2f}, {1:.2f}".format(point.X, point.Y)) #print the x and y cords

            partnum += 1 #increase the partnum by 1 each iteration












