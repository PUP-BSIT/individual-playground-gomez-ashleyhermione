"""
successful = False
for number in range (3):
   print ("Attempt")
   if successful:
     print ("Successful")
     break
else:
    print ("attempted 3 times and failed")
"""

"""
 #Sum of Numbers in a List
def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Example usage
print(sum_of_list([1, 2, 3, 4, 5]))  # Output: 15
"""
"""
 #Find the Largest Number in a List
def largest_number(numbers):
    if not numbers:  # Handle case for empty list
        return None
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# Example usage
print(largest_number([3, 6, 2, 8, 4]))  # Output: 8
"""

"""
def count_even_odd(numbers):
    even_count = 0
    odd_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count

# Example usage
print(count_even_odd([1, 2, 3, 4, 5, 6]))  # Output: (3, 3)
"""

"""
# Reverse a List
def reverse_list(items):
    reversed_list = []
    for i in range(len(items) - 1, -1, -1):
        reversed_list.append(items[i])
    return reversed_list

# Example usage
print(reverse_list([1, 2, 3, 4, 5]))  # Output: [5, 4, 3, 2, 1]
"""

