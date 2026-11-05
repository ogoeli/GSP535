#import the arcpy env
import arcpy
arcpy.env.overwriteOutput = True

#set the working directory to the EX08
arcpy.env.workspace = r'C:\Users\ope4\OneDrive - Northern Arizona University\Desktop\ACADEMIC_SEMSTER\FALL 2026\GSP 535 - PROGRAMMING FOR GIS\WEEK11\Ignore\PythonScripting_Ex08_Data\Ex08'

infc = "airports.shp" #the input dataset

outfc = "airports_anchorage.shp" #the output dataset file name

delim_field = arcpy.AddFieldDelimiters(infc, "COUNTY") #used to add proper field delimiters when creating query expressions.

sql_exp = delim_field + " = 'Anchorage Borough'" #create a query expression

arcpy.Select_analysis(infc, outfc, sql_exp) #Extracts features from an input feature, and stores them in an output feature class.


#delim_field = arcpy.AddFieldDelimiters(fc, "COUNTY") 

#1) What does the above line do? 
#the above line is a Field delimiter. This returns the properly formatted field name for the shapefile stored in fc and the field is COUNTY

#sql_exp = delim_field + " = 'Anchorage Borough'"

#2) What are the values of variables delim_field and sql_exp after these two lines are executed? 
#for the delim_field shapefile, this above line returns COUNTY without quotation marks as the field delimiter.

#3) Given the up-to-date arcpy, create a simplified and valid query expression that serves the purpose of the above two lines of code (2 points) 
#sql_exp = '"COUNTY" = \'Anchorage Borough\''
#This directly specifies the field and the attribute value being queried. and cause less confusion and creation of variables
