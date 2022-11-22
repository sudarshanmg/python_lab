# Write your code here :-)
a = [[1,2,3],[4,5,6],[7,8,9]]

res = 0
for i in range(3):
    for j in range(3):
        if i == j:
            res += a[i][j]

print(res)
