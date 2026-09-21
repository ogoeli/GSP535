#get height and weight from user
wh = input("Enter your weight in kg and height in m (separated by a space): ").split()
print(wh)

#seperate the the two values collected from users
weight, height = float(wh[0]), float(wh[1])
print(weight, height) 

#calculate BMI
bmi = round(weight / (height ** 2), 1)
#print(f"Your BMI is: {bmi}")

#else if statement to print BMI range
if bmi < 18.5:
    print(f"Your BMI is: {bmi}. You are classified as underweight.")
elif 18.5 <= bmi <= 24.9:
    print(f"Your BMI is: {bmi}. You are at a healthy weight.")
elif 25 <= bmi <= 29.9:
    print(f"Your BMI is: {bmi}. You are classified as overweight.")
else:
    print(f"Your BMI is: {bmi}. You are classified as obese.")