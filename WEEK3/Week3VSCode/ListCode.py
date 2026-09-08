#student list
students = ['Alex', 'Jacob', 'Jennifer', 'David', 'Andrew', 'John', 'Kevin', 'Clay', 'Kimberly', 'Jill',
'Joseph', 'Donitza', 'Andrew', 'Cory', 'Vincent', 'Nathan', 'Robert', 'Brandon', 'Olusegun']
print(len(students)) #get number of items in the list

#add item to end of list
print(students.append("Joseph"))
print(students)

#add item to start of list
print(students.insert(0,"Chris"))
print(students)

#count how mnay times an item appeared in the list
AndCount = students.count("Andrew")
print(AndCount)

#index of 1st Andrew
print(students.index("Andrew"))

#index of 2nd Andrew
print(students.index("Andrew", 6)) #since the 1st Andrew fell in 5th index, i seartched from 6th index till the end of the list

#1st 5 items in the list
print(students[:5])

#last 5 items in the list
print(students[-5:])

#remove 1st occurence of an item and place it at the end of the list
ReAnd = str("Andrew")
students.remove(ReAnd)
students.append(ReAnd)
print(students)

#sort the list in ascending order
students.sort()
print(students)

#sort the list in descending order
students.sort(reverse=True)
print(students)