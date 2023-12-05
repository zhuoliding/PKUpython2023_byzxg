n = int(input())
list1 = []
for i in range(n):
    list1.append(list(map(int,input().split())))
a =0
b = 0
for i in range(n):
    a += list1[i][0]
    b += list1[i][1]
if b == 0:
    print()
else:
    c = str(int(a/b*100*1000))
    if int(c[-1]) <= 4:
        print(f'{0.01*int(a/b*100*100):.2f}','%',sep = '')
    else:
        print(f'{0.01 * int(a / b * 100 * 100+1):.2f}', '%', sep='')