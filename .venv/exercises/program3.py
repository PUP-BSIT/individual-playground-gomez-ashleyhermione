# Program to find the highest of three numbers

# Take input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Check which number is the highest
if num1 >= num2 and num1 >= num3:
    print("The highest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("The highest number is:", num2)
else:
    print("The highest number is:", num3)
