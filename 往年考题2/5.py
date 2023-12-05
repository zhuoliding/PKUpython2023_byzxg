n = int(input())
list1 = list(map(int,input().split()))
for x in list1:
    c = list1.count(x)
    if c % 2 != 0:
        print(x)
        break
