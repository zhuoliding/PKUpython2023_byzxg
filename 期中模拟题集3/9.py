n,m = map(int,input().split())
list1 = [[0 for _ in range(m+2)]]
for i in range(n):
    list1.append([0]+list(map(int,input().split()))+[0])
list1.append([0 for _ in range(m+2)])
#print(list1)
sum = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if list1[i][j] == 1:
            list2 = [list1[i-1][j],list1[i+1][j],list1[i][j+1],list1[i][j-1]]
            if list2.count(1) == 0:
                sum += 4
            elif list2.count(1) == 1:
                sum += 3
            elif list2.count(1) == 2:
                sum += 2
            elif list2.count(1) == 3:
                sum += 1
print(sum)
