import Arcpy
arcpy.env.workspace = "D:/Ex03/Study.gdb"

fclist = arcpy.listFeatureClasses()
for fc in fclist
    result = arcpy.management.GetCount(fc)
    count = result.GetOutput(0)
      print("Number of features in feature class '{0}': {1}".format(fc, count))