# 1 + 2 = 3 , 1,2 are operands and + is operator
from sqlite3.dbapi2 import Binary

# Arithmetic Operators

a = 12
b = 2
c = -11
d = 13
e = -2

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a%b)

# Floored Division , considers until . , if negative number rounds to negative.

print(d//b)
print(c//b)
print(d//e)
print(c//e)

# **************************************************************************************************

# Comparison Operators 


print(a == b)
print(a <= b)
print(a >= b)
print(a != b)
print(a < b)
print(a > b)


# **************************************************************************************************

# Assignment Operators 

f = a + b
f = f + a
f += a
f -= a 
f *= a
f /= a
f **= a
f //= a

print(f)


# **************************************************************************************************

# Binary Operators 

b1 = int('00111100', 2)
b2 = int('00011101', 2)



print((b1 & b2).__format__("b"))

print(bin(b2))

