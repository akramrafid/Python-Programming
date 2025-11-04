'dictionary and sets'

# Dictionary and Sets in Python 
# Creating a dictionary
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(person)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
# Accessing elements in a dictionary
print(person['name'])  # Output: 'Alice'
print(person.get('age'))  # Output: 30
# Modifying elements in a dictionary        
person['age'] = 31
print(person)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York'}
# Adding elements to a dictionary
person['email'] = 'alice@example.com'
print(person)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'email': 'alice@example.com'} 
# Removing elements from a dictionary
del person['city']
print(person)  # Output: {'name': 'Alice', 'age': 31, 'email': 'alice@example.com'}
# Creating a set
fruits_set = {'apple', 'banana', 'cherry'}  
print(fruits_set)  # Output: {'banana', 'cherry', 'apple'} (order may vary)
# Adding elements to a set      
fruits_set.add('date')
print(fruits_set)  # Output: {'banana', 'cherry', 'apple', 'date'} (order may vary)
# Removing elements from a set  
fruits_set.remove('banana')
print(fruits_set)  # Output: {'cherry', 'apple', 'date'} (order may vary)   
# Checking membership in a set
print('apple' in fruits_set)  # Output: True    
print('banana' in fruits_set)  # Output: False
# Iterating over a dictionary       
for key, value in person.items():
    print(f"{key}: {value}")    
# Output: name: Alice, age: 31, email: alice@example.com    
# Iterating over a set
for fruit in fruits_set:
    print(fruit)    
# Output: cherry, apple, date (order may vary)
# Dictionary comprehension to create a new dictionary
squared_dict = {x: x**2 for x in range(5)}
print(squared_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
nested_tuples = ((1, 2), (3, 4), (5, 6))
print(nested_tuples[0])      # Output: (1, 2)   
print(nested_tuples[1][1])   # Output: 4    
# Nested lists and tuples
nested_list_tuple = [[(1, 2), (3, 4)], [(5, 6), (7, 8)]]
print(nested_list_tuple[0][1])      # Output: (3, 4)   
print(nested_list_tuple[1][0][1])   # Output: 6 
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}       
# Tuple unpacking in a dictionary
for key, value in squared_dict.items():
    print(f"{key}: {value}")    
# Output: 0: 0, 1: 1, 2: 4, 3: 9, 4: 16
# Set comprehension to create a new set
squared_set = {x**2 for x in range(5)}
print(squared_set)  # Output: {0, 1, 4, 9, 16}  
# Output: 0, 1, 4, 9, 16 (order may vary)   
for num in squared_set:
    print(num)  
# Output: 0, 1, 4, 9, 16 (order may vary)