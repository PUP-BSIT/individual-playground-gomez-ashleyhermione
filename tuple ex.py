#Given a tuple of numbers, return the first and the last elements.
"""
def first_and_last(numbers):
    return (numbers[0], numbers[-1])

# Test the function
numbers = (10, 20, 30, 40, 50)
print(first_and_last(numbers))  # Output: (10, 50)
"""

"""
# Count Occurrences in a Tuple
def count_occurrences(words, target_word):
    return words.count(target_word)

# Test the function
words = ("apple", "banana", "apple", "cherry", "apple")
target_word = "apple"
print(count_occurrences(words, target_word))  # Output: 3

"""

"""
# Find Maximum and Minimum in a Tuple
def min_and_max(numbers):
    return (min(numbers), max(numbers))

# Test the function
numbers = (10, 20, 5, 40, 25)
print(min_and_max(numbers))  # Output: (5, 40)




dict = { "message": "Hello world!" }
dict["language"] = "english"
print(dict)


dict = { "message": "Hello world!" }
dict["message"] = "Hi There!"
print(dict)


response_data = {
 "status_code": 200,
 "countries": ["Philippines","Japan","China"],
 "cities": {
   "Philippines": "Manila",
   "Japan": "Tokyo",
   "Korea": "Seoul",
 },
}
"""
response = (200,
        {'Content-Type': 'application/=json'},
        '{name : : "Alice}')
status_code, headers, body = response
print (type(status_code), )