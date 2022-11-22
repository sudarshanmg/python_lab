# Write your code here :-)
#greatest of 3 numbers
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

if(a >= b):
    if(a >= c):
        print(a)
    else:
        print(c)
else:
    if(b >= c):
        print(b)
    else:
        print(c)
