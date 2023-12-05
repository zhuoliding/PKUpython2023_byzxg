n,m = map(int,input().split())
list2 = []
while n != 0 and m != 0:
    list1 = list(map(int,input().split()))
    k = 0
    while list1.count(0) < n-1:
        u = 0
        while u < m-1:
            if list1[k] > 0:
                k += 1
                k = k % n
                u += 1
            elif list1[k] == 0:
                k += 1
                k = k % n
        while list1[k] == 0:
            k = (k+1)% n
        if list1[k] != 0:
            list1[k] -= 1
            k += 1
            k = k%n

    c= max(list1)
    ind = list1.index(c)
    list2.append(ind)
    n,m = map(int,input().split())
for x in list2:
    print(x+1)




