#import the arcpy env
import arcpy

#set the working directory to the EX05
arcpy.env.workspace = r'C:\Users\ope4\OneDrive - Northern Arizona University\Desktop\ACADEMIC_SEMSTER\FALL 2026\GSP 535 - PROGRAMMING FOR GIS\WEEK7\Ignore\PythonScripting_Ex05_Data\Ex05'

# Allow ArcPy to overwrite existing output files
arcpy.env.overwriteOutput = True

#Clip the bike routes layer using the parks layer as the clip boundary
#save the result to bike_clip.shp
newclip = arcpy.Clip_analysis("bike_routes.shp", 
"parks.shp", "bike_clip.shp") 

#Get the number of features (records) in the clipped bike routes shapefile
fcount = arcpy.GetCount_management("bike_clip.shp")

#Get the number of messages returned by the Clip tool
msgCount = newclip.messageCount

#Print the last message returned by the Clip tool
print(newclip.getMessage(msgCount-1))
