#import the arcpy env
import arcpy
arcpy.env.overwriteOutput = True

#set the working directory to the EX05
arcpy.env.workspace = r'C:\Users\ope4\OneDrive - Northern Arizona University\Desktop\ACADEMIC_SEMSTER\FALL 2026\GSP 535 - PROGRAMMING FOR GIS\WEEK9\Ignore\Midterm\Oil_Project.gdb'

# make a feature layer from the parcel feature class for use
# by the SelectLayerByLocation() tool
parcel_layer = arcpy.management.MakeFeatureLayer('Parcels', 'parcel_layer')

# list well paths in the well_data feature dataset
#wild card - B* finds all dataset that starts with B
#the feature type is a 'line'
#the feature_dataset is the feature class containing the well dats lines.
well_path_list = arcpy.ListFeatureClasses('B*', 'Line', 'Well_Data') 
print(well_path_list)

for well_path in well_path_list:   # for each well path, do the following:
# create an output well buffer name for use by the Buffer() tool
    wellbuf = "Buffers/" + well_path + "_buffer"

    # buffer the current well path by 200 feet
    well_buffer = arcpy.analysis.Buffer(well_path, wellbuf, '200 FEET')

    # select parcels that intersect the well path buffer
    parcels_selected = arcpy.management.SelectLayerByLocation(parcel_layer, 'INTERSECT', well_buffer)

    # create a file name (full path) for an output csv file
    parcel_csv = r'C:\Users\ope4\OneDrive - Northern Arizona University\Desktop\ACADEMIC_SEMSTER\FALL 2026\GSP 535 - PROGRAMMING FOR GIS\WEEK9\Ignore\Midterm\output\parcels.csv'
    
    # call the CopyRows() tool to export a csv file from the selected parcels
    arcpy.management.CopyRows(parcels_selected, parcel_csv)
    filecsv = open(parcel_csv, "r") #open csv file for reading  


    #create a file name (full) for an output mailing list
    mailing_txt = r'C:\Users\ope4\OneDrive - Northern Arizona University\Desktop\ACADEMIC_SEMSTER\FALL 2026\GSP 535 - PROGRAMMING FOR GIS\WEEK9\Ignore\Midterm\output'
    mailing_txt = mailing_txt + '\\' + 'mailing_list_' + well_path + ".txt" #construct the file path for the ouput txt file for each well path
    filetxt = open(mailing_txt, "w") #open txt file for writing 

    # calls the readlines() method which returns a list of content in the csv
    lines = filecsv.readlines()
    filecsv.close() # closes the file since the file object is no longer needed
    lines.pop(0) # remove the first line (a file header) from the lines list

    # write the header for the txt file created
    #filetxt.write()
    
    #extract addresses from the parcel_csv file and
    #write them into the mailing list file
    #(Refer to Lecture 5 Examples 8 & 9 and Lab 4)
    #for each line in the csv file, write its cotent to a txt file
    for line in lines: # starts a for loop to iterate over each line
        split_line = line.split(',') #split the lines by ","
        address = split_line[19] #get the 19th index which is the PROP_ADD
        #filetxt = open(mailing_txt, "w") #open txt file for writing 
        filetxt.write(address + '\n')
        
    filetxt.close() #close the txt file after writing.

    #deleting intermediate datasets
print('Cleaning up ...')
arcpy.management.Delete(parcel_csv) #delete the parcel_csv file

print('Spatial analysis completed successfully.')

print('Please find the resulting outputs in database ouput folder.')


