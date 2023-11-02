list1 = list(map(int,input().split()))
list1.sort()
max_num = max(list1)
for i in range(1, max_num + 1):
    if i not in list1:
        print(i)
        break
    