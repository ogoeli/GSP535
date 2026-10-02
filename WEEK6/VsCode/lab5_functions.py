#create a function named volume() with two parameters length, width and height
def volume(length, width, height):
    vol = (length * width * height) #calculate the volume of blocks 
    return vol  # and return the result stored in vol

#use the function
x = volume(50, 10, 20) #calling the function with 3 parameters
print(x)


#create a function listsum() with one parameter 
def listsum(mylist):
    total = 0
    for n in mylist:
        total += n
    return total

#use the function
numbers = [1, 2, 3, 4, 5]
x = listsum(numbers)
print(x)


#create a function named reverse
def reverse(string):
    rev = ""
    for ch in string:
        rev = ch + rev
    return rev

#use the function
text = "Hello, World!"
x = reverse(text)
print(x)

