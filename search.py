# Write your code here :-)
nums = [4,5,6,6,3,2,6,7,8,4,3,2,1]

key = int(input("Enter the number to be searched: "))

#Linear search
flag = 0
for i in range(len(nums)):
    if(nums[i] == key):
        print(key, "found in position",i+1)
        flag = 1

if(flag == 0):
    print("Key not found")

#Binary search
def bin_search(lis, l, r, key):
    if(l > r):
        return -1
    m = (l + r)//2
    if(lis[m] == key):
        print("m = ", m)
        return m
    elif(lis[m] > key):
        return bin_search(lis, l, m-1, key)
    else:
        return bin_search(lis, m+1, r, key)

lis = [1,2,3,4,5]
pos = bin_search(lis, 0, 4, 2)

if(pos != -1):
    print(pos)
else:
    print("Key not found")
