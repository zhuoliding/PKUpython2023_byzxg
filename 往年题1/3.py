m,n = map(int,input().split())
mat = []
for i in range(m):
    mat.append(list(map(int,input().split())))
num = 0
for i in range(m):
    for j in range(n):
        if mat[i][j] == 1:
            num += 1
print(num)

