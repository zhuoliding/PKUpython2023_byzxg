n = int(input())
list1 = []
for i in range(n):
    list1.append(list(map(int,input().split())))
for i in range(n):
    num = list1[i][0] - list1[i][1]*list1[i][2]
    if num >= 0:
        print(num)
    else:
        print(0)
