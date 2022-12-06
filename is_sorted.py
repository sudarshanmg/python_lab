# Write your code here :-)
def is_sorted(lis):
    temp = lis.copy()
    temp.sort()
    if temp == lis:
        return True
    return False

print(is_sorted([1,2,3,4]))
