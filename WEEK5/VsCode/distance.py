# uses a variable to hold the file path 
# opens the file for reading. note: "r" is optional 
filepath = "C:\\Users\\ope4\\OneDrive - Northern Arizona University\\Desktop\\ACADEMIC_SEMSTER\\FALL 2026\\GSP 535 - PROGRAMMING FOR GIS\\WEEK5\\Ignore\\coordinates.txt" 
file = open(filepath, "r")   

#open file for writing
filewrite = "C:\\Users\\ope4\\OneDrive - Northern Arizona University\\Desktop\\ACADEMIC_SEMSTER\\FALL 2026\\GSP 535 - PROGRAMMING FOR GIS\\WEEK5\\Ignore\\distances.txt" 
filehold = open(filewrite, "w")   

# remove the first line (a file header) from the lines list 
header = file.readline()  

# write the new header
filehold.write("X1,Y1,X2,Y2,DIST\n")

for line in file: 
    # split the line into a list of strings 
    coordinates = line.split(",") 
    # convert the strings to floats 
    x1 = float(coordinates[0]) 
    y1 = float(coordinates[1]) 
    x2 = float(coordinates[2]) 
    y2 = float(coordinates[3]) 

    # calculate the distance between the two points 
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5 

    # write the distance to the output file 
    filehold.write(str(x1) + "," + str(y1) + "," + str(x2) + "," + str(y2) + "," + str(round(distance, 1)) + "\n")

file.close()
filehold.close()
