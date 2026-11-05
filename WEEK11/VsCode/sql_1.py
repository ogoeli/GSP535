#import the arcpy env
import arcpy
arcpy.env.overwriteOutput = True

#set the working directory to the EX08
arcpy.env.workspace = r'C:\Users\ope4\OneDrive - Northern Arizona University\Desktop\ACADEMIC_SEMSTER\FALL 2026\GSP 535 - PROGRAMMING FOR GIS\WEEK11\Ignore\PythonScripting_Ex08_Data\Ex08'

fc = "airports.shp" #this assigns the shapefile data in the GDB to a variable named fc

sql_exp = '"TOT_ENP" > 100000' # search with exact value expression where the TOT_ENP greater than 100000 rows, get assigns to sql_exp 

cursor = arcpy.da.SearchCursor(fc, ["NAME"], sql_exp) # the following calls the SearchCursor class to create a cursor

for row in cursor: # loop through rows in the cursor created above
    print(row[0]) # print the row data starting from index 0

#sql_exp = '"TOT_ENP" > 100000' 
#1) What does this line do?
# the lines searches with exact value expression whereTOT_ENP greater than 100000 rows, get assigns to sql_exp 

#2) Why is "TOT_ENP" quoted by a pair of double quotation marks but 100000 is not? 
# because the string values must be single quoted inside the expr. but  Numbers must not be quoted inside the expr.  
# and  A basic query expression is a string, (so it must be enclosed in a pair of quotation marks 

#3) Can we take off the double quotation marks around TOT_ENP?
#No, the double quotation indicates the TOT_ENP is a string value enclosed in the exp.
