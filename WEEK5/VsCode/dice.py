#import random umber
import random   
# imports the random module 
x = random.randint(1, 6) # calls the randint() function to generate an integer  
# between 1 and 6, then assigns the result to variable x 

#asks the users for a guess between 1 and 6
user = int(input("Enter a guess between 1 and 6:\n"))

#if the guess is not equal to the users guess, 
# it will ask the user to enter another guess until they get it right
while x != user:
  user = int(input("Enter another guess between 1 and 6:\n"))
print("You win!")