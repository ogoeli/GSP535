class Student:   #declares the class "student"
    def __init__(self, firstname, lastname): # declares function __init__() 
        self.firstname = firstname
        self.lastname = lastname

    def getFullname(self): #declares a function named getFullname with "self" as the parameter
        return self.firstname + " " + self.lastname

# test the Student class 
if __name__ == "__main__":      # checks if the script is run as a main module      
    Student1 = Student("John", "Smith")          #instantiates a student object (Student1)      
    print(Student1.getFullname())               #call the getFullname() method of student1 to print full name of the student 
 
    Student2 = Student("Ogonna", "Eli")                #instantiates a student object (student2)
    print(Student2.getFullname())      #call the getFullname() method of student2 to print full name of the student


#create a polyline class
import math #import the math module for the sqrt() method to calculate the length of the polyline

#create the Polyline class
class Polyline:
    def __init__(self):
        self.points = []

    def addPoint(self, x, y):
        self.points.append((x, y))

    #insertPoint(index, x, y) method to insert a point at a specific index
    def insertPoint(self, index, x, y):
        self.points.insert(index, (x, y))

    def getPoint(self, index):
        return self.points[index]

    def delPoint(self, index):
        del self.points[index]

    def getLength(self):
        length = 0
        for i in range(len(self.points) - 1):
            length += math.sqrt((self.points[i + 1][0] - self.points[i][0]) ** 2 + (self.points[i + 1][1] - self.points[i][1]) ** 2)
        return length


# test the Polyline class
if __name__ == "__main__":
    #test the addPoint() method and getLength() method
    polyline1 = Polyline()
    polyline1.addPoint(0, 0)
    polyline1.addPoint(3, 4)
    polyline1.addPoint(6, 0)
    polyline1.addPoint(0, 8)
    polyline1.addPoint(9, 0)
    print(f"Length of the polyline 1: {polyline1.getLength()}")

    #test the insertPoint() method and getLength() method
    polyline2 = Polyline()
    polyline2.insertPoint(0, 1, 1)
    polyline2.addPoint(3, 9)
    print(f"Length of the polyline 2: {polyline2.getLength()}")

    #test the getPoint() method
    polyline3 = Polyline()
    polyline3.addPoint(0, 0)
    polyline3.addPoint(3, 4)
    polyline3.addPoint(6, 0)
    print(f"Point at index 2: {polyline3.getPoint(2)}") 

    #test the delPoint() method
    polyline4 = Polyline()
    polyline4.addPoint(0, 0)
    polyline4.addPoint(3, 4)
    polyline4.addPoint(6, 0)
    polyline4.delPoint(1)
    print(f"Remaining point at polyline 4: {polyline4.points}") 