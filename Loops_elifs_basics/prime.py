# Write your code here :-)
# prime nums upto 100
def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if(n % i != 0):
            continue
        else:
            return False
    return True

for i in range(1, 101):
    if(isPrime(i) == True):
        print(i)

