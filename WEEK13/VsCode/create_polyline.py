#import the arcpy env
import arcpy
import fileinput 
import os
arcpy.env.overwriteOutput = True

#set the working directory to the EX09
ws = r'C:\Users\ope4\OneDrive - Northern Arizona University\Desktop\ACADEMIC_SEMSTER\FALL 2026\GSP 535 - PROGRAMMING FOR GIS\WEEK13\Ignore\PythonScripting_Ex09_Data\Ex09'

arcpy.env.workspace = ws 

newfc = "newpolyline.shp" #describe a new feature class

sr = r'C:\Users\ope4\OneDrive - Northern Arizona University\Desktop\ACADEMIC_SEMSTER\FALL 2026\GSP 535 - PROGRAMMING FOR GIS\WEEK13\Ignore\PythonScripting_Ex09_Data\Ex09\dams.prj'

arcpy.CreateFeatureclass_management(ws, newfc,"Polyline", spatial_reference = sr) #create empty new fc, as a polyline and dams crs

#read the txt file with cordinates
infile = os.path.join(ws, "coordinates.txt") #The coordinates in this text file will be used to create the vertices for a polyline

with arcpy.da.InsertCursor(newfc, ["SHAPE@"]) as cursor: #use of an insert cursor to create new rows and an array object to contain the point objects.
    array = arcpy.Array()

    for line in fileinput.input(infile): #iterate over the text file to create a point object for each line in the text file.  
        ID, X, Y = line.split() #split each txt file line into 3 variables ID, X and Y
        array.add(arcpy.Point(X, Y)) #add the X and Y content of each line to an array

    cursor.insertRow([arcpy.Polyline(array)]) #create a polyline using the array created from the loop

    fileinput.close() #close out the file
