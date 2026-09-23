#asks the users for a number
user = input("Enter 3 or more digit number:\n") 
print(user)

#create a variable to hold the reversed number
result = ""

#create a for loop to iterate through the user input and reverse the number
for n in user: 
    result = n + result 
print(result)