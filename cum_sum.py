# Write your code here :-)
def csum(lis):
    res = [lis[0]]
    for i in range(1,len(lis)):
        res.append(lis[i]+res[i-1])
    return res

print(csum([1,2,3]))
