import math
coor = list(map(float,input().split()))
x = 0
y = 0
for i in range(0,len(coor)//2):
    x += coor[2*i]
    y += coor[2*i+1]
c = math.sqrt(x*x+y*y)
print(f'{c:.4f}')



