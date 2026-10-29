#import the arcpy env
import arcpy
import os
arcpy.env.overwriteOutput = True

#set the working directory to the EX06
arcpy.env.workspace = r'C:\Users\ope4\OneDrive - Northern Arizona University\Desktop\ACADEMIC_SEMSTER\FALL 2026\GSP 535 - PROGRAMMING FOR GIS\WEEK10\Ignore\PythonScripting_Ex06_Data\Ex06'
ws = r'C:\Users\ope4\OneDrive - Northern Arizona University\Desktop\ACADEMIC_SEMSTER\FALL 2026\GSP 535 - PROGRAMMING FOR GIS\WEEK10\Ignore\PythonScripting_Ex06_Data\Ex06'

#sets the output geodatabase to the fgdb folder
fgdb = "Copy.gdb"

#this creates a file geodatabase in a folder
#with ws the work dir and fgdb the new create geodatabase.
arcpy.CreateFileGDB_management(ws, fgdb)

#set the workspace to the data folder
arcpy.env.workspace = ws

#arcpy.ListFeatureClasses() function
#returns a Python list of feature class names in the current workspace
fclist = arcpy.ListFeatureClasses()

# a for loop to list all feature in the list
#extracts the basename and join the paths from the ws to the geodatabase created and attache the name
#the last line copies the feature from the old one to the new feature,
#copy geometry and attributes from an existing feature class, layer,
#or table view to a new feature class
for fc in fclist: #start of the loop
    fcname = arcpy.da.Describe(fc)["baseName"] #a line to get fc basename
    newfc = os.path.join(ws, fgdb, fcname) #oin the paths from the ws to the geodatabase created and attache the name
    arcpy.CopyFeatures_management(fc, newfc) #the last line copies the feature from the old one to the new feature,
