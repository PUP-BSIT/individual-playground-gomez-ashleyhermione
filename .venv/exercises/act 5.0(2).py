
def inverted(dict):
    inverted = {}  
    for key in dict:  
        inverted[dict[key]] = key 
    return inverted

data = {'a':1, 'b':2, 'c':3}
result = inverted(data)
print(result) 