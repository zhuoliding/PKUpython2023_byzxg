number = int(input())
import math
e = 1
for i in range(1,number+1):
    e += 1/math.factorial(i)
print(f'{e:.15f}')

