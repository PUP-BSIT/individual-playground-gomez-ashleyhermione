# Program to check if a character is a vowel or consonant

# Take input from the user
char = input("Enter a character: ")

# Convert to lowercase to make comparison easier
char = char.lower()

# Check if the character is a vowel
if char in 'aeiou':
    print("The character is a vowel.")
elif char.isalpha():  # Check if it's a letter
    print("The character is a consonant.")
else:
    print("Invalid input. Please enter a letter.")
