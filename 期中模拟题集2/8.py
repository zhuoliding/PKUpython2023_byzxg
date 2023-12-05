t= int(input())
list1 =[]
for i in range(t):
    list1.append(list(map(int,input().split())))
def find_num(a,b):
    sum = 0
    for i in range(a,b+1):
        stri= str(i)
        u = 1
        for k in range(1,len(stri)+1):
            if k%2 == 0 and int(stri[k-1]) % 2 != 0:
                u = 0
                break
            elif k%2 != 0 and int(stri[k-1]) % 2 == 0:
                u = 0
                break
        sum += u
    return sum

for i in range(t):
    print(find_num(list1[i][0],list1[i][1]))





