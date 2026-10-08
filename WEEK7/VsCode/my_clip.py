import arcpy
arcpy.env.workspace = r'C:\Users\ope4\OneDrive - Northern Arizona University\Desktop\ACADEMIC_SEMSTER\FALL 2026\GSP 535 - PROGRAMMING FOR GIS\WEEK7\Ignore\PythonScripting_Ex05_Data\Ex05'
arcpy.env.overwriteOutput = True 
newclip = arcpy.Clip_analysis("bike_routes.shp", 
"parks.shp", "bike_clip.shp") 
fcount = arcpy.GetCount_management("bike_clip.shp") 
msgCount = newclip.messageCount 
print(newclip.getMessage(msgCount-1))
