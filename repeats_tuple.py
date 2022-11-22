# Write your code here :-)

'''
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
'''

tups = (1,2,5,3,2,4,5,6,3,2.1,3,4)
c=[]

for i in tups:
    if(tups.count(i) > 1):
        if i not in c:
            c.append(i)
print(c)
