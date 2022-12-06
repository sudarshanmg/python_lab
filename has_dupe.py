# Write your code here :-)
def has_dupe(lis):
    lis.sort()
    for i in range(1,len(lis)):
        if(lis[i-1] == lis[i]):
            return True
    return False

print(has_dupe([2,1,2]))

