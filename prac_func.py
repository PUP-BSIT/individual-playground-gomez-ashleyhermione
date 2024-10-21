
'''
input_colors = int(input("Enter an index [0]-[4]: "))
colors = ['purple', 'yellow', 'pink', 'orange', 'black' ]

if 0 <= input_colors < len(colors):
  print(f"the color of you chose is {colors[input_colors]}") 
'''


def get_num():
    numbers = []
    for i in range(5):
     num = int(input("Enter a number: "))
     numbers.append(num) # yung append add yon
    return numbers

def sum_in_list(numbers):
   return sum(numbers)

def average_in_list(numbers):
   return sum_in_list(numbers) / len(numbers)   

def highest_in_list(numbers):
   return max(numbers)

def main():
   numbers = get_num()

   print("Sum of the numbers: ", sum_in_list(numbers))
   print("Average of the numbers:", average_in_list(numbers))
   print("Highest number is: ", highest_in_list(numbers) )
   
main()