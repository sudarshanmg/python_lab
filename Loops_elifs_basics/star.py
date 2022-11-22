# Write your code here :-)
#star patterns
for i in range(5):
    print("*" * 5)
print("=========")
for i in range(5):
    print("*" * (5 - i))
print("=========")
for i in range(5):
    print("*" * i)

print("=========")

for j in range(0, 5):
    for i in range(1+j,5):
        print(i, end=" ")
    print(" ")

