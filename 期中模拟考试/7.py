import math
num = input()
def sushu(n):
    b = int(n)
    if b == 1:
        return False
    else:
        for i in range(2,int(math.sqrt(b))+1):
            if b % i == 0:
                return False
        else:
            return True
def super_sushu(n):
    if len(n) == 1:
        return sushu(n)
    else:
        return sushu(n) and super_sushu(n[:-1])

if super_sushu(num):
    print('YES')
else:
    print('NO')



