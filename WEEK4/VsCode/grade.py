#get name, section and grade from user 
nsg = input("Enter your name, section number, and points earned: ").split(',')
print(nsg)
 
#seperate the the two values collected from users
name, section = nsg[0], int(nsg[1])
points_earned = float(nsg[2])
print(f"Name: {name}, Section: {section}, Points earned: {points_earned}")

#else if statement to check the grade and print the corresponding letter grade
if section == 435:
    points = 600
elif section == 535:
    points = 700

#calculate the percentage of the grade
percentage = round((points_earned / points) * 100, 2)
print(f"Percentage: {percentage}%")

#else if statement to check the percentage and print the corresponding letter grade
if percentage >= 90:
    letter_grade = "A"
elif percentage >= 80:
    letter_grade = "B"
elif percentage >= 70:
    letter_grade = "C"
elif percentage >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

print(f"SECTION: GSP{section}")
print(f"STUDENT: {name}")
print(f"GRADE: {letter_grade}")


