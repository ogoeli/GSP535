#get temperature from user
proTemp = input("Enter the temperature: ")
print(proTemp)
#get the last character which is the unit
sepCF =  float(proTemp[:-1]) #get values excluding the last 
print(sepCF)

#except the last character.
unit = proTemp[-1]
print(unit)

#else if statement to check if the unit is C or F
if unit == "C":
    #convert to Fahrenheit
    F = round((sepCF * 9/5) + 32, 1)
    print(f"Temperature {sepCF}° Celsius is {F}° Fahrenheit.")
elif unit == "F":
    #convert to Celsius
    C = round((sepCF - 32) * 5/9, 1)
    print(f"Temperature {sepCF}° Fahrenheit is {C}° Celsius.")