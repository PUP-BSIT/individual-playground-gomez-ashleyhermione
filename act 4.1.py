
'''
index = int(input("Enter your desired index: "))
fav_foods = ['Fries', 'Ice cream', 'Carbonara', 'Curry', 'Chicken']
print (index, fav_foods)


fruits = ["apple", "banana", "cherry"]
fruits.remove()
print(fruits)

fruits = ["Strawberries", "Spinach", "Kale"]
vegetables = ["Tomatoes", "Celery", "Potatoes"]
food = [fruits, vegetables]
print(food)


for number in range(5, 10, 2):
    print(number)




message = "Starting loop"
while message != "exit":
    print(message)
    message = input("Enter your message: ")
   
print("Loop Ended")


for number in range(1, 11):
    if number == 7:
        continue
    print(number)

for number in range(1, 11):
    if number == 7:
        break
    print(number)

def greet():
    global message
    message = "Hello World!"

greet()
print(message)


message = "Hello World!"
def greet():
    #global message
    message = "Hi There!"
    print(message)

greet()
print(message)


def greet(msg):
    print(f"Greetings: {msg}")

greet("Hello World!")


def celsius_to_fahrenheit(celsius):
    farenheit = (celsius * 9/5) + 32
    return farenheit

celsius = celsius_to_fahrenheit(36)
print(celsius)
'''

def get_sum_of_digits(value):
    if not value.isdigit():
        print("Not a number.")
        return 0

    tens_digit = int(value[0])
    ones_digit = int(value[1])
    return tens_digit + ones_digit

user_input = input("Enter a 2 digit number: ")
print(get_sum_of_digits(user_input))


    
