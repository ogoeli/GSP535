#import the arcpy env
import arcpy

#set the working directory to the EX05
arcpy.env.workspace = r'C:\Users\ope4\OneDrive - Northern Arizona University\Desktop\ACADEMIC_SEMSTER\FALL 2026\GSP 535 - PROGRAMMING FOR GIS\WEEK7\Ignore\PythonScripting_Ex05_Data\Ex05'

#assign parks.shp to in_fc
in_fc = "parks.shp" 

#assign the centriod created from parks shp to out_fc
out_fc = "parks_centroid.shp" 

#if statement to perform the feature to point if ArcInfo is found
if arcpy.ProductInfo() == "ArcInfo": 
    arcpy.FeatureToPoint_management(in_fc, out_fc) 
else: 
    print("An ArcInfo license is not available.")
