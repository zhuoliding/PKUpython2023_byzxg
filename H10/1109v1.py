import math
xs = input()
def su(x):
    if x == '1':
        return False
    else:
        for i in range(2,int(math.sqrt(int(x)))+2):
            if int(x) % i == 0 and int(x) // i >= 2:
                return False
        else:
            return True
def super_su(x):
    if len(x) == 1:
        return su(x)
    else:
        return super_su(x[:-1]) and su(x)
    
if super_su(xs) == True:
    print('YES')
else:
    print('NO')
