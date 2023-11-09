number = int(input())
import math
e = 0
for i in range(number):
    e += 1/math.factorial(i)
print(f'{e:.8f}')


