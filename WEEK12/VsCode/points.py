#import the arcpy env
import arcpy
arcpy.env.overwriteOutput = True

#set the working directory to the EX09
arcpy.env.workspace = r'C:\Users\ope4\OneDrive - Northern Arizona University\Desktop\ACADEMIC_SEMSTER\FALL 2026\GSP 535 - PROGRAMMING FOR GIS\WEEK12\Ignore\PythonScripting_Ex09_Data\Ex09'

fc = "dams.shp" #assign the dams shapefile to fc variable

with arcpy.da.SearchCursor(fc, ["SHAPE@XY"]) as cursor: #use SearchCursor to read data from the feature class created above. this also retrives the XY of each geom and holds it as cursor

    for row in cursor: #a for loop to loop through each feature in the cursor

        x, y = row[0] #assign the XY values from each row to seperate variables X and Y

        print("{0:.3f}, {1:.3f}".format(x, y)) #print the output with a comma
