# Write your code here :-)
nums = []

for i in range(3):
    a = int(input("Enter a number: "))
    nums.append(a);

avg = sum(nums)/len(nums)
sigma = sum(nums)

m = 0
for i in nums:
    m += (i - avg)**2

sd = (m/(len(nums)-1))**0.5
var = sd**2
print(sigma, avg, sd, var)
