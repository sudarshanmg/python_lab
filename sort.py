# Write your code here :-)
num = []

for i in range(5):
    a = int(input("Enter a number: "))
    num.append(a)

num.sort()
print(num)
num.sort(reverse = True)
print(num)
