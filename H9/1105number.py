import math
a = int(input())
b = int(input())
number = 0
for n in range(a,b+1):
    c = 0
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            c = 1
    if c == 0:
        number += 1
print(number)
