# 1. Write a Python program to print the number entered by user only if the number entered is negative.
a = float(input("Print number please "))
if a <0:
    print(f"You input negative number {a}")
else:
    print(f"You input positive number {a}")
  
# 2. Write a Python program to check if the value a is less than 20 or not.
b = float(input("Plese input number"))
if b<20:
 print("You input less than 20")
elif b>20:
 print("You input number more than 20")
else: 
 print("You make mistake") 

# 3. Write a Python program to check if a given number is Zero or Not.
c =int(input("Plese input some information"))
print(f"Given iformation is {c==0}") 
# 4. Write a Python program to check if a given number is Even or Odd.
d = int(input("Plese input some information"))
if ((d%2)>0):
    print("You input Even")
else:
    print("You input Odd number")
    
# 5. Write a Python program to find largest number among three numbers entered by user.

num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))
num3 = float(input("Enter 3rd number: "))

if (num1 >= num2) and (num1 >= num3):
   lnum = num1
elif (num2 >= num1) and (num2 >= num3):
   lnum = num2
else:
   lnum = num3

print("The largest number among",num1,",",num2,"and",num3,"is: ",lnum)

