#import the arcpy env
import arcpy
arcpy.env.overwriteOutput = True

#set the working directory to the EX05
arcpy.env.workspace = r'C:\Users\ope4\OneDrive - Northern Arizona University\Desktop\ACADEMIC_SEMSTER\FALL 2026\GSP 535 - PROGRAMMING FOR GIS\WEEK7\Ignore\PythonScripting_Ex03_Data\Ex03\Study.gdb'

#soil input feature
soil_in = 'soils'

#basin input features
basin_in = 'basin'

xy_tolerance = ""

#basin buffer output feature
basin_buff_out = r'C:\Users\ope4\OneDrive - Northern Arizona University\Desktop\ACADEMIC_SEMSTER\FALL 2026\GSP 535 - PROGRAMMING FOR GIS\WEEK7\Ignore\PythonScripting_Ex03_Data\Ex03\Study.gdb\basin_buffer'

#soil clip output feature
soil_clip_out = r'C:\Users\ope4\OneDrive - Northern Arizona University\Desktop\ACADEMIC_SEMSTER\FALL 2026\GSP 535 - PROGRAMMING FOR GIS\WEEK7\Ignore\PythonScripting_Ex03_Data\Ex03\Study.gdb\soils_clip'

#final output of Darnen loam soil
darnen_soil_out = r'C:\Users\ope4\OneDrive - Northern Arizona University\Desktop\ACADEMIC_SEMSTER\FALL 2026\GSP 535 - PROGRAMMING FOR GIS\WEEK7\Ignore\PythonScripting_Ex03_Data\Ex03\Study.gdb\darnen_soils'

#buffer the basin
print('Buffering basin ...')
arcpy.Buffer_analysis(basin_in, basin_buff_out, "400 METERS",  "", "", "ALL")

#clip the soil feature
print('Clipping soils ...')
arcpy.Clip_analysis(soil_in, basin_buff_out, soil_clip_out, xy_tolerance) 

#select feature where "MUNAME" = 'DARNEN LOAM'
print('Selecting Darnen Loam soil ...')
where_clause =  '"MUNAME" = \'DARNEN LOAM\''
arcpy.analysis.Select(soil_clip_out, darnen_soil_out, where_clause)

#count how many darnen soil created
print('Counting Darnen Loam polygons ...')
result = arcpy.management.GetCount(darnen_soil_out)
count = int(result[0])
print(f'The output layer includes {count} Darnen soil polygons.')

#deleting intermediate datasets
print('Cleaning up ...')
arcpy.management.Delete(basin_buff_out) #delete the basin buffer feature
arcpy.management.Delete(soil_clip_out) #delete the soil clip feature
print('Spatial analysis completed successfully.')

print('Please find the resulting feature class in database Study.gdb.')



