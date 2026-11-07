#import the arcpy env
import arcpy
arcpy.env.overwriteOutput = True

#set the working directory to the EX05
arcpy.env.workspace = r'C:\Users\ope4\OneDrive - Northern Arizona University\Desktop\ACADEMIC_SEMSTER\FALL 2026\GSP 535 - PROGRAMMING FOR GIS\WEEK9\Ignore\Midterm\Oil_Project.gdb'

# make a feature layer from the parcel feature class for use
# by the SelectLayerByLocation() tool
print('Creating a parcel layer ...')
try:
    #try the following block of code 
    parcel_layer = arcpy.management.MakeFeatureLayer('Parcels', 'parcel_layer')
except TypeError:   # catches data type exception 
    print("Error: Incorrect data type") 
except Exception as e:  # catches any other exceptions 
    print(e) 

# list well paths in the well_data feature dataset
#wild card - B* finds all dataset that starts with B
#the feature type is a 'line'
#the feature_dataset is the feature class containing the well dats lines.
print('creating a feature dataset for the well data ...')
well_path_list = arcpy.ListFeatureClasses('B*', 'Line', 'Well_Data') 
print(f'Well Data paths are {well_path_list}')


for well_path in well_path_list:   # for each well path, do the following:
# create an output well buffer name for use by the Buffer() tool
    wellbuf = "Buffers/" + well_path + "_buffer"

    # buffer the current well path by 200 feet
    well_buffer = arcpy.analysis.Buffer(well_path, wellbuf, '200 FEET')

    # select parcels that intersect the well path buffer
    parcels_selected = arcpy.management.SelectLayerByLocation(parcel_layer, 'INTERSECT', well_buffer)

    #create a file name (full) for an output mailing list
    mailing_txt = r'C:\Users\ope4\OneDrive - Northern Arizona University\Desktop\ACADEMIC_SEMSTER\FALL 2026\GSP 535 - PROGRAMMING FOR GIS\WEEK9\Ignore\Midterm\output'
    mailing_txt = mailing_txt + '\\' + 'mailing_list_' + well_path + ".txt" #construct the file path for the ouput txt file for each well path
    filetxt = open(mailing_txt, "w") #open txt file for writing 

     # create a search cursor to retrieve property addresses
    with arcpy.da.SearchCursor(parcels_selected, ["Prop_add"]) as cursor:

        # extract addresses and write them into the mailing list file
        for row in cursor:
            address = row[0]
            filetxt.write(str(address) + '\n')

    # close the txt file after writing
    filetxt.close()

print('Spatial analysis completed successfully.')

print('Please find the resulting outputs in database output folder.')
