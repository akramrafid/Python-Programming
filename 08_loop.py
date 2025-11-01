'Loops in Python'

# A simple for loop that iterates over a list of numbers
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)  

# A for loop that iterates over a string and prints each character
char_string = "hello"
for char in char_string:
    print(char) 

# A for loop that iterates over a dictionary and prints keys and values
sample_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in sample_dict.items():
    print(f"Key: {key}, Value: {value}")    
people = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 35)]
for person in people:
    print(person.age)  # Output: 30, 25, 35 

print(ages)  # Output: [30, 25, 35]     

# A for loop that iterates over a set and prints each element
sample_set = {1, 2, 3, 4}   
for elem in sample_set:
    print(elem) 
# A for loop that iterates over a tuple and prints each element
sample_tuple = (1, 2, 3, 4) 
for elem in sample_tuple:
    print(elem) 