n,m = map(int,input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int,input().split())))
def next_time(i,j):
    if m > 2 and n > 2:
        if 0 < i < m - 1 and 0 < j < n - 1:
            near = [matrix[j][i - 1], matrix[j - 1][i - 1], matrix[j - 1][i], matrix[j + 1 - n][i - 1],
                    matrix[j - n + 1][i], matrix[j - 1][i - m + 1], matrix[j][i - m + 1], matrix[j - n + 1][i - m + 1]]
        elif i == 0 and j == 0:
            near = [matrix[0][1], matrix[1][0],matrix[1][1]]
        elif i == 0 and j == n - 1:
            near = [matrix[n - 1][1], matrix[n - 2][0],matrix[n-2][1]]
        elif i == m - 1 and j == n - 1:
            near = [matrix[n - 1][m - 2], matrix[n - 2][m - 1],matrix[n-2][m-2]]
        elif i == m - 1 and j == 0:
            near = [matrix[0][m - 2], matrix[1][m - 1],matrix[1][m-2]]
        elif i == 0:
            near = [matrix[j][1], matrix[j - 1][0], matrix[j - n + 1][0], matrix[j - 1][1], matrix[j - n + 1][1]]
        elif i == m - 1:
            near = [matrix[j][m - 2], matrix[j - 1][m - 1], matrix[j - n + 1][m - 1], matrix[j - 1][m - 2],
                    matrix[j - n + 1][m - 2]]
        elif j == 0:
            near = [matrix[0][i - 1], matrix[0][i - m + 1], matrix[1][i], matrix[1][i - 1], matrix[1][i - n + 1]]
        elif j == n - 1:
            near = [matrix[n - 1][i - 1], matrix[n - 1][i - m + 1], matrix[n - 2][i], matrix[n - 2][i - 1],
                    matrix[n - 2][i - m + 1]]
    elif m == 2 and n > 2:
        if i == 0 and j == 0:
            near = [matrix[0][1], matrix[1][0], matrix[1][1]]
        elif i == 0 and j == n - 1:
            near = [matrix[n - 1][1], matrix[n - 2][0], matrix[n - 2][1]]
        elif i == m - 1 and j == n - 1:
            near = [matrix[n - 1][m - 2], matrix[n - 2][m - 1], matrix[n - 2][m - 2]]
        elif i == m - 1 and j == 0:
            near = [matrix[0][m - 2], matrix[1][m - 1], matrix[1][m - 2]]
        elif i == 0:
            near = [matrix[j][1], matrix[j - 1][0], matrix[j - n + 1][0], matrix[j - 1][1], matrix[j - n + 1][1]]
        elif i == m - 1:
            near = [matrix[j][m - 2], matrix[j - 1][m - 1], matrix[j - n + 1][m - 1], matrix[j - 1][m - 2],
                    matrix[j - n + 1][m - 2]]
    elif m > 2 and j == 2:
        if i == 0 and j == 0:
            near = [matrix[0][1], matrix[1][0], matrix[1][1]]
        elif i == 0 and j == n - 1:
            near = [matrix[n - 1][1], matrix[n - 2][0], matrix[n - 2][1]]
        elif i == m - 1 and j == n - 1:
            near = [matrix[n - 1][m - 2], matrix[n - 2][m - 1], matrix[n - 2][m - 2]]
        elif i == m - 1 and j == 0:
            near = [matrix[0][m - 2], matrix[1][m - 1], matrix[1][m - 2]]
        elif j == 0:
            near = [matrix[0][i - 1], matrix[0][i - m + 1], matrix[1][i], matrix[1][i - 1], matrix[1][i - n + 1]]
        elif j == n - 1:
            near = [matrix[n - 1][i - 1], matrix[n - 1][i - m + 1], matrix[n - 2][i], matrix[n - 2][i - 1],
                    matrix[n - 2][i - m + 1]]
    elif m == 2 and n == 2:
        if i == 0 and j == 0:
            near = [matrix[0][1], matrix[1][0], matrix[1][1]]
        elif i == 0 and j == n - 1:
            near = [matrix[n - 1][1], matrix[n - 2][0], matrix[n - 2][1]]
        elif i == m - 1 and j == n - 1:
            near = [matrix[n - 1][m - 2], matrix[n - 2][m - 1], matrix[n - 2][m - 2]]
        elif i == m - 1 and j == 0:
            near = [matrix[0][m - 2], matrix[1][m - 1], matrix[1][m - 2]]
    elif m == 1 and n > 2:
        if j == 0 or j == n-1:
            near = []
        else :
            near = [matrix[j-1][0],matrix[j+1][0]]
    elif m > 2 and n == 1:
        if i == 0 or i == m-1:
            near = []
        else:
            near = [matrix[0][i-1],matrix[0][i+1]]
    else:
        near = []






    num = near.count(1)
    if num < 2:
        return 0
    elif num == 3:
        return 1
    elif num > 3:
        return 0
    else:
        return matrix[j][i]


for i in range(n):
    for j in range(m-1):
        print(next_time(j,i),end = ' ')
    print(next_time(m-1,i))



