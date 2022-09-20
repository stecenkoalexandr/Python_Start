print("Hello World!")
# ---------------------------------------------------------------------------------------------------
print("Here we wilbe study Python")

print("I thought Python is very useful language")

print("Many companies use Python for their projects")

print("Igor", "Oleg", "Dima", sep='\n')
# Намагаємось все писати в одному рядку, для того щоб мінімалізувати ресурси
# ------------------------------------------------------------------------------------------------------
# Exercise 3. Write a Python-script to reads values for the length and width of a rectangle and returns the area of the rectangle

a = int(input("Dear user please input lenght"))
b = int(input("Dear user please input width"))
print(f"Area of the rectangle will be {a*b}")

# Exercise 4 Write a program that requests the user to enter two numbers and  prints the sum, product, difference and quotient of the two numbers

c = int(input("Please input number#1"))
d = int(input("Please input number#2"))
print(f"Sum  will be {c+d}\n Product will be {c*d} n\ Difference will be{c-d} n\ Quotient will be{c%d}")
# ------------------------------------------------------------------------------------------------------------
# Exercise 5. Write a program that reads in the radius of a circle and prints the circle’s diameter, circumference and area. Use the constant value 3.14159 for π.
# Do these calculations in output statements.

radius = int(input("Please input the radius of circle"))
PI = 3.14159
print(f"Circle diamentr{radius*2} \n Circle will be {PI*radius*2} \r Area of circle will be {PI*radius**2}")

