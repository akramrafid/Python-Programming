# A conditional expression allows you to evaluate something based on a condition being true or false.
# The syntax is: <true_value> if <condition> else <false_value>

# Example 1: Basic conditional expression
age = 20    
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult

# Example 2: Using conditional expression in a function
def check_even_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

print(check_even_odd(10))  # Output: Even
print(check_even_odd(7))   # Output: Odd

# Example 3: Nested conditional expressions
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C"
print(grade)  # Output: B

# Example 4: Conditional expression with lists
numbers = [1, 2, 3, 4, 5]
parity = ["Even" if num % 2 == 0 else "Odd" for num in numbers] 
print(parity)  # Output: ['Odd', 'Even', 'Odd', 'Even', 'Odd']

# Example 5: Using conditional expression in lambda functions
is_positive = lambda x: "Positive" if x > 0 else "Non-positive"
print(is_positive(10))   # Output: Positive
print(is_positive(-5))   # Output: Non-positive
print(is_positive(0))    # Output: Non-positive
