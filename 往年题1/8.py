n,m = map(int,input().split())
list1 = []
for i in range(n):
    list1.append(list(map(int,input().split())))
list1.sort(key = lambda x : -x[1])
for i in range(len(list1)):
    if list1[i][0] <= m:
        m = m-list1[i][0]
    else:
        k = i
        break
else:
    k = len(list1)
if k != 0:
    print(k)
else:
    print(0)
