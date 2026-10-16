import arcpy #arcpy is case senstive so not "Arcpy"
arcpy.env.workspace = r'C:\Users\ope4\OneDrive - Northern Arizona University\Desktop\ACADEMIC_SEMSTER\FALL 2026\GSP 535 - PROGRAMMING FOR GIS\WEEK7\Ignore\PythonScripting_Ex03_Data\Ex03\Study.gdb' #changed location

fclist = arcpy.ListFeatureClasses() #make the because the ArcPy function uses a capital L and F and C.

for fc in fclist: #added a colon to the end of the for loop
    result = arcpy.management.GetCount(fc)
    count = result.getOutput(0) #Python is case-sensitive, so changed the GetOuput to getOutput
    print("Number of features in feature class '{0}': {1}".format(fc, count)) #fixed the print() indentation
