#import the arcpy env
import arcpy
import os
arcpy.env.overwriteOutput = True

#set the working directory to the EX09
ws = r'C:\Users\ope4\OneDrive - Northern Arizona University\Desktop\ACADEMIC_SEMSTER\FALL 2026\GSP 535 - PROGRAMMING FOR GIS\WEEK13\Ignore\PythonScripting_Ex09_Data\Ex09'

arcpy.env.workspace = ws 

newfc = "newSchoolPoints.shp" #describe a new feature class

srIn = arcpy.SpatialReference(4326) #point geom crs

srOut = arcpy.SpatialReference(102649) #blank shp crs

arcpy.CreateFeatureclass_management(ws, newfc,"Point", spatial_reference = srOut) #create empty new fc, as a POINT and dams crs

 # Run AddField 4 times  for two new fields
arcpy.management.AddField(newfc, 'NAME', "TEXT", field_length = 50)
arcpy.management.AddField(newfc, 'ADDRESS', "TEXT", field_length = 50)
arcpy.management.AddField(newfc, 'ZIP', "TEXT", field_length = 10)
arcpy.management.AddField(newfc, 'DISTRICT', "SHORT")
   
#read the txt file with cordinates
infile = os.path.join(ws, "schools.txt") #The coordinates in this text file will be used to create the vertices for a point

with arcpy.da.InsertCursor(newfc, ["Id", "SHAPE@", "NAME", "ADDRESS", "ZIP", "DISTRICT"]) as cursor: #use of an insert cursor to create new rows and an array object to contain the point objects.
    with open(infile) as f: #open the input file
        next(f) #skip the header before the loop starts
    
        for line in f: #iterate over the text file to create a point object for each line in the text file.
            ID, X, Y, NAME, ADDRESS, ZIP, DISTRICT = line.strip().split(',') #split each txt file line into 3 variables ID, X and Y
            X = float(X) #convert from string to float
            Y = float(Y) #convert from string to float
            ID = int(ID) #convert the ID to an interger
            DISTRICT = int(DISTRICT) #convert from string to integer
            geom = arcpy.Point(X, Y) #add the X and Y content of each line to an array
            pointGeom = arcpy.PointGeometry(inputs = geom, spatial_reference = srIn) #create a point geometry from the txt x and y
            pointOut = pointGeom.projectAs(srOut) #reproject the output file
            fields = [ID, pointOut, NAME, ADDRESS, ZIP, DISTRICT] #the field header for the new file created
            #row_values = [(fields)]

            
            cursor.insertRow(fields) #create a point shapefile using the values created from the loop

        f.close() #close out the file
