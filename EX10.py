input_str = input("Input: ") 

string = {} 

for occur in input_str: 
	if occur in string: 
		string[occur] += 1
	else: 
		string[occur] = 1

print ("Output: \n "+ str(string)) 

