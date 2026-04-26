# find the circumference of a circle
#find the area of a circle
pi = 3.14
radius = int(float(input("Enter the radius of the circle: ")))
area = pi * radius**2
circumference = 2 * pi * radius

print(f"The area of the circle is: {round(area)} cm^2")
print(f"The circumference of the circle is: {round(circumference)} cm")

