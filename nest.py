# Write your code here :-)
def nested_sum(lis):
    res = 0
    for i in lis:
        res = res+sum(i)
    print(res)
t = [[1,2,3],[4], [5]]
nested_sum(t)
