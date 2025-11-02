'List and Tuple Operations in Python'

# Creating a list
fruits = ['apple', 'banana', 'cherry']
print(fruits)  # Output: ['apple', 'banana', 'cherry']  
# Accessing elements in a list
print(fruits[0])  # Output: 'apple'
print(fruits[1])  # Output: 'banana'
print(fruits[-1]) # Output: 'cherry'
# Modifying elements in a list
fruits[1] = 'blueberry'
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']
# Adding elements to a list
fruits.append('date')
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'date']
# Removing elements from a list
fruits.remove('banana')
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'date']
# Creating a tuple
coordinates = (10, 20)
print(coordinates)  # Output: (10, 20)
# Accessing elements in a tuple
print(coordinates[0])  # Output: 10
print(coordinates[1])  # Output: 20
# Tuples are immutable, so we cannot modify them
# However, we can create a new tuple based on an existing one
new_coordinates = (coordinates[0], 30)
print(new_coordinates)  # Output: (10, 30)
# Converting a list to a tuple
fruits_tuple = tuple(fruits)
print(fruits_tuple)  # Output: ('apple', 'blueberry', 'cherry', 'date')
# Converting a tuple to a list
coordinates_list = list(coordinates)
print(coordinates_list)  # Output: [10, 20]
# Slicing a list
sliced_fruits = fruits[1:3] 
print(sliced_fruits)  # Output: ['blueberry', 'cherry']
# Slicing a tuple
sliced_coordinates = coordinates[0:1]
print(sliced_coordinates)  # Output: (10,)
# Iterating over a list
for fruit in fruits:
    print(fruit)
# Output: apple, blueberry, cherry, date
# Iterating over a tuple
for coord in coordinates:
    print(coord)
# Output: 10, 20
# List comprehension to create a new list
squared_numbers = [x**2 for x in range(5)]  
print(squared_numbers)  # Output: [0, 1, 4, 9, 16]
# Tuple unpacking
x, y = coordinates
print(x)  # Output: 10
print(y)  # Output: 20  
# Nested lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0])      # Output: [1, 2, 3]       
print(matrix[1][2])   # Output: 6
# Nested tuples
point = ((1, 2), (3, 4))    
print(point[0])      # Output: (1, 2)
print(point[1][1])   # Output: 4
# List methods
fruits.sort()
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'date']
fruits.reverse()    
print(fruits)  # Output: ['date', 'cherry', 'blueberry', 'apple']
count = fruits.count('apple')
print(count)  # Output: 1   
index = fruits.index('cherry')
print(index)  # Output: 1   
length = len(fruits)
print(length)  # Output: 4
print(len(coordinates))  # Output: 2
# Checking membership
print('banana' in fruits)  # Output: False
print(10 in coordinates)   # Output: True
# Iterating with index using enumerate
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")    
# Output: Index: 0, Fruit: date
#         Index: 1, Fruit: cherry
#         Index: 2, Fruit: blueberry
#         Index: 3, Fruit: apple    
# Unpacking in loops
pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
for number, word in pairs:  
    print(f"Number: {number}, Word: {word}")        
    # Output: Number: 1, Word: one
    #         Number: 2, Word: two
    #         Number: 3, Word: three
    