#this script imports the arcpy env, sets the workspace,
#arcpy.ListFeatureClasses() function returns a Python list of feature class names in the current workspace
#a for loop to loop through each feature in the feature class and extract the
#datatype for the feature, the name and the shapetype. then print out the information

import arcpy #import the arcpy env
arcpy.env.overwriteOutput = True

#set the working directory to the EX06
arcpy.env.workspace = r'C:\Users\ope4\OneDrive - Northern Arizona University\Desktop\ACADEMIC_SEMSTER\FALL 2026\GSP 535 - PROGRAMMING FOR GIS\WEEK10\Ignore\PythonScripting_Ex06_Data\Ex06'

cities = r'C:\Users\ope4\OneDrive - Northern Arizona University\Desktop\ACADEMIC_SEMSTER\FALL 2026\GSP 535 - PROGRAMMING FOR GIS\WEEK10\Ignore\PythonScripting_Ex06_Data\Ex06\cities.shp'

#question 5 of question 1 solution [txr doc content]
#myshp = arcpy.da.Describe(cities)
#print(myshp)
#myshp["shapeType"]


fclist = arcpy.ListFeatureClasses() #calls the ListFeatureClasses() to returns a Python list of feature class names in the current workspace
print(fclist) #this prints out the features contained in the feature class in our working directory 

for fc in fclist: #start of the loop
    fcdesc = arcpy.da.Describe(fc) # call function Describe() to describe the fearure in the fclist
    dtype = fcdesc["dataType"] # call a fcdesc[] line to get the fc datatype
    name = fcdesc["name"] # call a fcdesc[] line to get the name of the fc 
    stype = fcdesc["shapeType"] # call a fcdesc[] line to get the shapetype of the fc
    print(f"{dtype} {name} has shapetype {stype}") #this prints out the result
    


