# Write your code here :-)
num = [1, "hey", 2.4, -1, "lol", 23, True, "dmwm"]

strings = []
bools = []
floats = []
ints = []

for i in range(len(num)):
    if type(num[i]) == type(2):
        ints.append(num[i])
    if type(num[i]) == type(2.4):
        floats.append(num[i])
    if type(num[i]) == type(''):
        strings.append(num[i])
    if type(num[i]) == type(True):
        bools.append(num[i])

print(ints, floats, strings, bools)
