import math
n = int(input())
posi = [[float(x) for x in input().split()] for _ in range(n)]
dis = [math.sqrt(posi[i][0]*posi[i][0]+posi[i][1]*posi[i][1]) for i in range(n)]
print(f'{min(dis):.2f}')