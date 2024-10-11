# Program to return the sum of the two digits of a 2-digit number

# Take input from the user
number = int(input("Enter a 2-digit number: "))

# Extract the tens and units digits
tens_digit = number // 10  # Floor division to get the tens digit
units_digit = number % 10  # Modulo to get the units digit

# Calculate the sum of the two digits
sum_of_digits = tens_digit + units_digit

# Print the result
print("The sum of the two digits is:", sum_of_digits)
