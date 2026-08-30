# Import math Library
import math

pie = math.pi

# Print the value of pi
print (f"pi: {pie}")

#ask user for radius
cly_rad = float(input("What is the radius of the cylinder?: "))
print(f"The radius of the cylinder is: {cly_rad}")

#ask user for height
cly_height = float(input("What is the height of the cylinder?: "))
print(f"The height of the cylinder is: {cly_height}")

#calculate the volume of the cylinder
cly_volume = round(pie * (cly_rad ** 2) * cly_height, 2)
print(f"The volume of the cylinder is: {cly_volume} cubic inches")
