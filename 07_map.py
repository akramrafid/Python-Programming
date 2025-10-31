'This is a map function example'

def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))

'Output the result'
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]


'Nested map example with lambda function'
nested_numbers = [[1, 2], [3, 4], [5, 6]]
nested_squares = list(map(lambda x: list(map(square, x)), nested_numbers))
print(nested_squares)  # Output: [[1, 4], [9, 16], [25, 36]]

'Using map with multiple iterables'
def add(x, y):
    return x + y    
list1 = [1, 2, 3]
list2 = [4, 5, 6]
summed_list = list(map(add, list1, list2))
print(summed_list)  # Output: [5, 7, 9]

'Using map with a string to convert characters to their ASCII values'
char_string = "hello"
ascii_values = list(map(ord, char_string))
print(ascii_values)  # Output: [104, 101, 108, 108, 111]

'Using map with a dictionary to get keys and values'
sample_dict = {'a': 1, 'b': 2, 'c': 3}
keys = list(map(lambda x: x[0], sample_dict.items()))   
values = list(map(lambda x: x[1], sample_dict.items()))
print(keys)    # Output: ['a', 'b', 'c']    
print(values)  # Output: [1, 2, 3]  
'Using map with a set to square each element'
sample_set = {1, 2, 3, 4}
squared_set = set(map(square, sample_set))
print(squared_set)  # Output: {16, 1, 4, 9} 
'Using map with a tuple to square each element'
sample_tuple = (1, 2, 3, 4) 
squared_tuple = tuple(map(square, sample_tuple))
print(squared_tuple)  # Output: (1, 4, 9, 16)   
'Using map with a range to square each number'
squared_range = list(map(square, range(1, 6)))
print(squared_range)  # Output: [1, 4, 9, 16, 25]   
'Using map with filter to square only even numbers'
even_numbers = filter(lambda x: x % 2 == 0, numbers)
squared_even_numbers = list(map(square, even_numbers))
print(squared_even_numbers)  # Output: [4, 16]  
'Using map with reduce to sum squared numbers'
from functools import reduce
sum_of_squares = reduce(lambda x, y: x + y, squared_numbers)
print(sum_of_squares)  # Output: 55 
'Using map with a custom class to get attribute values'
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
people = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 35)]
ages = list(map(lambda person: person.age, people)) 
print(ages)  # Output: [30, 25, 35]
'Using map with a generator to square numbers'  
def number_generator(n):
    for i in range(1, n + 1):
        yield i 
squared_gen = list(map(square, number_generator(5)))
print(squared_gen)  # Output: [1, 4, 9, 16, 25]
'Using map with itertools to square numbers from two ranges'
import itertools
range1 = range(1, 4)  # [1, 2, 3]
range2 = range(4, 7)  # [4, 5, 6]
squared_itertools = list(map(square, itertools.chain(range1, range2)))  
print(squared_itertools)  # Output: [1, 4, 9, 16, 25, 36]
'Using map with pandas to square a DataFrame column'
import pandas as pd
df = pd.DataFrame({'numbers': [1, 2, 3, 4, 5]})
df['squared'] = list(map(square, df['numbers']))    
print(df)
# Output:
#    numbers  squared
# 0        1        1
# 1        2        4
# 2        3        9
# 3        4       16
# 4        5       25
