class Person:   #declares the class "person"
    firstname = "" #declares the first name property
    lastname = "" #declares the last name property
    occupation = "" #declares the occupation property
    
    def greet(self): #declares a function named greet with "self" as the parameter
        print("Hi, My name is " + self.firstname + " " + self.lastname)
        print("I am a " + self.occupation)

# test the Person class 
if __name__ == "__main__":      # checks if the script is run as a main module      
    person1 = Person()          #instantiates a person object (person1)      
    person1.firstname = "John"   #sets the firstame property of person1 to "John"      
    person1.lastname = "Smith"   #sets the lastname property of person1 to "Smith"     
    person1.occupation = "Actor"  # sets the occupation property 
    person1.greet()               #call the greet() method of person1 to print the greeting message    
 
    person2 = Person()                #instantiates a person object (person2)
    person2.firstname = "Ogonna"         #sets the firstname property of person2 to "Ogonna"
    person2.lastname = "Eli"        #sets the lastname property of person2 to "Eli"
    person2.occupation = "Student"  # sets the occupation property 
    person2.greet()        #call the greet() method of person2 to print the greeting message           
