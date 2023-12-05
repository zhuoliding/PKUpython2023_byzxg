[n,k] = list(map(int,input().split()))
list1 = [x for x in range(1,n+1)]
list2 = [1]+[0 for _ in range(n-1)]
matrix_1 = [[list1[i-j] for i in range(n)] for j in range(n,0,-1)]
matrix_0 = [[list2[i-j] for i in range(n)] for j in range(n)]
matrix_out = [[0 for i in range(n)] for j in range(n)]
def mul(matrix_1,matrix_2):
    matrix_out = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                matrix_out[i][j] += matrix_1[i][k]*matrix_2[k][j]
    return matrix_out
matrix_f = matrix_0
if k != 0:
    for i in range(k):
        matrix_f = mul(matrix_f,matrix_1)
for i in range(n):
    for j in range(n-1):
        print(matrix_f[i][j],end = ' ')
    print(matrix_f[i][n-1])







