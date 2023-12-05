n = int(input())
list1 = []
while n != 0:
    list1.append(list(map(int,input().split())))
    n = int(input())

for x in list1:
    x.sort()
    print(x[len(x)//2])
