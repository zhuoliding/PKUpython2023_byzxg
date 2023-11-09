coor = list(map(int,input().split()))
import math
x = 0
y = 0
theta = 0
for i in range(0,len(coor)//2):
    theta += coor[2*i]/180*math.pi
    x += math.cos(theta)*coor[2*i+1]
    y += math.sin(theta)*coor[2*i+1]
dis = math.sqrt(x*x+y*y)
print(f'{dis:.4f}')
    


