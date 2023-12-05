T = int(input())
list2 = []
for i in range(T):
    n, m = map(int, input().split())
    list1 = []
    for i in range(n):
        list1.append(list(map(int, input().split())))
    num = 0
    for i in range(n):
        if float(list1[i].count(1)) >= m / 2:
            num += 1
    list2.append(num)
for x in list2:
    print(x)

