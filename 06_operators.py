## Arithmetic Operators
a = 10  
b = 3
print("Addition:", a + b)          # 13
print("Subtraction:", a - b)       # 7  
print("Multiplication:", a * b)    # 30
print("Division:", a / b)          # 3.3333
print("Floor Division:", a // b)   # 3
print("Modulus:", a % b)           # 1
print("Exponentiation:", a ** b)   # 1000

## Comparison Operators
x = 5
y = 10
print("Equal:", x == y)            # False
print("Not Equal:", x != y)        # True
print("Greater Than:", x > y)      # False
print("Less Than:", x < y)         # True
print("Greater Than or Equal:", x >= y)  # False
print("Less Than or Equal:", x <= y)     # True

## Logical Operators
p = True
q = False
print("Logical AND:", p and q)     # False
print("Logical OR:", p or q)       # True
print("Logical NOT:", not p)       # False

## Assignment Operators
c = 5
c += 3  # c = c + 3
print("c after += 3:", c)          # 8
c *= 2  # c = c * 2
print("c after *= 2:", c)          # 16
c -= 4  # c = c - 4
print("c after -= 4:", c)          # 12
c /= 3  # c = c / 3
print("c after /= 3:", c)          # 4.0
c %= 3  # c = c % 3
print("c after %= 3:", c)          # 1.0

## Bitwise Operators
m = 6  # 110 in binary
n = 3  # 011 in binary
print("Bitwise AND:", m & n)       # 2 (010 in binary)
print("Bitwise OR:", m | n)        # 7 (111 in binary)
print("Bitwise XOR:", m ^ n)       # 5 (101 in binary)
print("Bitwise NOT:", ~m)          # -7 (inverts bits)
print("Left Shift m by 1:", m << 1) # 12 (1100 in binary)
print("Right Shift m by 1:", m >> 1) # 3 (011 in binary)
