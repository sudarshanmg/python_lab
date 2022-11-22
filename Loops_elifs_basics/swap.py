# Write your code here :-)
# swapping using a third var
a = 1
b = 2
c = a
a = b
b = c
print("a: " + str(a))
print("b: " + str(b))

# swappping using + -
a = a + b
b = a - b
a = a - b
print("+ -")
print("a: " + str(a))
print("b: " + str(b))

# swappping using + -
a = a * b
b = a // b
a = a // b
print("* /")
print("a: " + str(a))
print("b: " + str(b))

# swapping using xor
a = a ^ b
b = a ^ b
a = a ^ b
print("^")
print("a: " + str(a))
print("b: " + str(b))
