
"""
ب م م 

Greatest Common Divisor(gcd)

"""
"""
#The function is ready to calculate the greatest common divisor

import math
bmm = math.gcd(18,15)
print("bmm is:", bmm)
"""

x = int(input("please enter a number:"))
y = int(input("please enter a number:"))
if abs(x)>abs(y):
    n = abs(x) 
else :
    n = y
for i in range (1,n+1):
    if x % i == 0 and y % i == 0:
        print (i)
        bmm = i
print("bmm is :",bmm)

