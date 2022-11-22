# Write your code here :-)
#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the first item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list
num = [4,2,5,4,2,3,5,3,3,7,5,3]

a = int(input("Enter a number that has to be removed from the list: "))
count = num.count(a)

for i in range(count):
        num.remove(a)

print(num)
