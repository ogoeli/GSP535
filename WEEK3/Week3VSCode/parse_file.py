#create the file path varibale
filepath = "D:/Data/Flagstaff/Roads.shp"
print(filepath)

#get the first letter which is the Drive
drive = filepath[0]
print(drive)

#get the directory folder path by taking last /
FinSlash = filepath.rfind("/") #get the index of the last /
print(FinSlash)
directory = filepath[0:FinSlash] #get strings from the start till the last /
print(directory)

#find the file name with extension
filename = filepath[FinSlash + 1:] #get values excluding the last / till the end of the string
print(filename)

#find the base name without the extension
periodIndex = filename.index(".") # find the index of the "."
print(periodIndex)
basename = filename[0:periodIndex] #print from the filename excluding the "."
print(basename)