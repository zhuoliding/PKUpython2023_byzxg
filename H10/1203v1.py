[n,m] = list(map(int,input().split()))
weight = list(map(int,input().split()))
list = []
for i in range(n-m):
    if weight[m+i] > weight[i]:
        list.append(sum(weight[i:m+i]))
if list == []:
    print(weight[n-m:n])
else:
    print(min(list))


