numbers = []
for i in range(5):
     num = int(input("Enter a number: ")) 
     numbers.append(num)

def sum_in_list(numbers):
     return sum(numbers)

def average_in_list(numbers):
     return sum_in_list(numbers) / len(numbers)

def highest_in_list(numbers):
     return max(numbers)

def factorial(num):
     if num == 0 or num == 1:
        return 1
     else:
        return num * factorial (num-1)
def main():
     print("Sum of the numbers: ", sum_in_list(numbers))
     print("Average of the numbers: ", average_in_list(numbers))
     print("Max of the numbers: ", highest_in_list(numbers))
     num = int(input("Enter a number: "))
     print(f"The factorial of {num} is:  {factorial(num)}")

main()

