import math
x = input()
p = 0
for i in range(0,len(x)):
    num = int(x[0:i+1])
    p = 0
    for j in range(2,int(math.sqrt(num))+2):
        if num%j == 0 and num//j != 1 or num == 1:
            p += 1
            break
    if p == 1:
        print('NO')
        break
if p == 0:
    print('YES')
    