n = int(input())
matrix = [input().split() for _ in range(n)]
list1 = []
list2 = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == '0':
            list1.append(i)
            list2.append(j)
for i in range(n):
    if i in list1:
        print('0 '*(n-1),0,sep='')
    else:
        for j in range(n-1):
            if j in list2:
                print(0,end=' ')
            else:
                print(matrix[i][j],end=' ')
        if n-1 in list2:
            print(0)
        else:
            print(matrix[i][n-1])

