# Write your code here :-)
a = input()
num = a.split(',')
for i in range(len(num)):
    num[i] = int(num[i])
print(list(num))
