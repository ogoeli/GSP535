#import the arcpy env
import arcpy
arcpy.env.overwriteOutput = True

#set the working directory to the EX06
arcpy.env.workspace = r'C:\Users\ope4\OneDrive - Northern Arizona University\Desktop\ACADEMIC_SEMSTER\FALL 2026\GSP 535 - PROGRAMMING FOR GIS\WEEK10\Ignore\PythonScripting_Ex06_Data\Ex06'

cities = r'C:\Users\ope4\OneDrive - Northern Arizona University\Desktop\ACADEMIC_SEMSTER\FALL 2026\GSP 535 - PROGRAMMING FOR GIS\WEEK10\Ignore\PythonScripting_Ex06_Data\Ex06\cities.shp'

#question 5 of question 1 solution [txr doc content]
#myshp = arcpy.da.Describe(cities)
#print(myshp)
#myshp["shapeType"]

#arcpy.ListFeatureClasses() function returns a Python list of feature class names in the current workspace
fclist = arcpy.ListFeatureClasses()
print(fclist) #this prints out the features contained in the feature class in our working directory 

#a for loop to loop through each feature in the feature class and extract the
#datatypenfor the feature, the name and the shapetype. then print out the information
for fc in fclist: #start of the loop
    fcdesc = arcpy.da.Describe(fc) #a line to describe the data property
    dtype = fcdesc["dataType"] #a line to get the fc datatype
    name = fcdesc["name"] # a line to get the name of the fc 
    stype = fcdesc["shapeType"] # a line to get the shapetype of the fc
    print(f"{dtype} {name} has shapetype {stype}") #this prints out the result
    


