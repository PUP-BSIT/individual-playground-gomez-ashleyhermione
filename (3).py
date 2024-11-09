# def dict_to_tuples(d)- Convert the dictionary into a list of tuples (key-value pairs)
def dict_to_tuples(d):
    return list(d.items())
 #d.items()-returns a view object of the dictionary's key-value pairs
 # list()-converts this view object into a list of tuples

example_dict = {'a': 1, 'b': 2, 'c': 3}
tuple_list = dict_to_tuples(example_dict)
print(tuple_list)  # Output: [('a', 1), ('b', 2), ('c', 3)]