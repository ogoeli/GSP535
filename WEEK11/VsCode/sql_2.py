#import the arcpy env
import arcpy
arcpy.env.overwriteOutput = True

#set the working directory to the EX08
arcpy.env.workspace = r'C:\Users\ope4\OneDrive - Northern Arizona University\Desktop\ACADEMIC_SEMSTER\FALL 2026\GSP 535 - PROGRAMMING FOR GIS\WEEK11\Ignore\PythonScripting_Ex08_Data\Ex08'

fc = "airports.shp" #this assigns the shapefile data in the GDB to a variable named fc

sql_exp = '"FEATURE" = \'Seaplane Base\''  # search with exact value expression where the TOT_ENP greater than 100000 rows, get assigns to sql_exp 

cursor = arcpy.da.SearchCursor(fc, ["NAME"], sql_exp) # the following calls the SearchCursor class to create a cursor

for row in cursor: # loop through rows in the cursor created above
    print(row[0]) # print the row data starting from index 0

#sql_exp = '"FEATURE" = \'Seaplane Base\'' 
#1) What does this line do?
# the lines searches with exact value expression where FEATURE is equal to Seaplane Base in the rows, get assigns to sql_exp 

#2) WWhy is "FEATURE" quoted by a pair of double quotation marks and \'Seaplane Base\' is surrounded by \'? 
#Field delimiters for shapefiles consist of double quotation marks
#a backslash within a string is interpreted as an escape character, 
#a signal that the next character is to be given a special interpretation [search pattern with wildcard]

#3) Can we take off the double quotation marks around FEATURE?
#No, the double quotation indicates the FEATURE is a Field delimiters for shapefiles enclosed in the exp.
