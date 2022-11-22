# Write your code here :-)

a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[1,2,3],[4,5,6],[7,8,9]]
c = []
for i in range(3):
    row = []
    for j in range(3):

        k = a[i][j] + b[i][j]
        row.append(k)
    c.append(row)

print(c)
