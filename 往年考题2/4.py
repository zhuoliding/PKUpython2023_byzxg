n,m = map(int,input().split())
list1 = list(map(int,input().split()))
sum = 0
num = 1
for i in range(len(list1)):
    if sum < m:
        sum += list1[i]
    else:
        sum = list1[i]
        num += 1
print(num)