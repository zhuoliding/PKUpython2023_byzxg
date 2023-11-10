import math
n = int(input())
b = int(math.sqrt(n))
a = 0
for i in range(2,b+1):
    if n%i == 0:
        a = 1
if a == 0:
    print('yes')
else:
    print('no')
