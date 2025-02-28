def first_max_key(dict):
    max_key = None
    max_value = None

    for key in dict:                                           
        if max_value is None or dict[key] > max_value: 
            max_value = dict[key]

    return max_key

data = {'John': 80, 'Alice': 92, 'Bob': 85, 'Charlie': 92}
result = first_max_key(data)
print(result)