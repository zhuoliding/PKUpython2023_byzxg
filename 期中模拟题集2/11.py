n,p = map(int,input().split())
list1 = []
for i in range(n):
    list1.append(int(input()))
list_out = []


def find(i,money):
    global stri
    if i == 0:
        c = money // list1[i]
        for j in range(c, -1, -1):
            stri = {}
            stri[0] = (str(list1[i]) + ' ') * j
            find(i + 1, money - j * list1[i])
    elif i == n-1:
        if money == 0:
            list_out.append(stri[n-2].strip(' '))
        elif money % list1[i] == 0:
            stri[n-1] = stri[n-2]+(str(list1[i]) + ' ')*(money//list1[i])
            list_out.append(stri[n-1].strip(' '))
    else:
        if money == 0:
            list_out.append(stri[i-1].strip(' '))
        else:
            c = money // list1[i]
            for j in range(c,-1,-1):
                stri[i] = stri[i-1] + (str(list1[i]) + ' ')*j
                find(i+1,money-j*list1[i])

find(0,p)
if list_out == []:
    print('NO')
else:
    for x in list_out:
        print(x)





