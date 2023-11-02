import math
list = input().split()
a = float(list[0])
b = float(list[1])
c = float(list[2])
delta = b*b-4*a*c
if a == 0 and b == 0:
    print('No Answer')
elif a == 0 and b != 0:
    print(f'{-c/b:.4f}')
elif delta < 0:
    print('No Answer')
elif delta == 0:
    print(f'{-b/(2*a):.4f}')
else:
    x1 = (-b-math.sqrt(delta))/(2*a)
    x2 = (-b+math.sqrt(delta))/(2*a)
    if x1 < x2:
        print(f'{x1:.4f}',f'{x2:.4f}')
    else:
        print(f'{x2:.4f}',f'{x1:.4f}')
