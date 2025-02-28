# Program to check if a number is odd, even, or zero

# Take input from the user
num = int(input("Enter a number: "))

# Check if the number is zero, even, or odd
if num == 0:
    print("The number is zero.")
elif num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
