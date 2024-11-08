# Problem 1: Check for Prime Number
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# User input and usage for Problem 1
num = int(input("Enter a number to check if it's prime: "))
print(f"Is {num} a prime number? {is_prime(num)}")


# Problem 2: Reverse a String
def reverse_string(s):
    return s[::-1]

# User input and usage for Problem 2
text = input("Enter a string to reverse: ")
print(f"The reverse of '{text}' is '{reverse_string(text)}'")


# Problem 3: Find the Greatest Common Divisor (GCD)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# User input and usage for Problem 3
num1 = int(input("Enter the first number for GCD: "))
num2 = int(input("Enter the second number for GCD: "))
print(f"The GCD of {num1} and {num2} is {gcd(num1, num2)}")


# Problem 4: FizzBuzz
def fizz_buzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

# User input and usage for Problem 4
n = int(input("Enter a number for FizzBuzz: "))
print("FizzBuzz result:", fizz_buzz(n))


# Problem 5: Find Unique Elements in a List
def unique_elements(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

# User input and usage for Problem 5
lst = input("Enter numbers separated by spaces to find unique elements: ")
lst = list(map(int, lst.split()))  # Convert input to a list of integers
print(f"Unique elements in the list: {unique_elements(lst)}")
