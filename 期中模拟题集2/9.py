import math

def GPA(x):
    if x >= 60:
        return 4-3*math.pow((10-x/10.0),2.5)/32
    else:
        return 0

def find_tot(k,score):
    sum = 0
    totk = 0
    for i in range(k):
        sum += dict[score[i][0]]*GPA(score[i][1])
        totk += dict[score[i][0]]
        averge = sum/totk
    return round(averge,4)

n = int(input())
dict = {}
for i in range(n):
    x,y = map(int,input().split())
    dict[x] = y
m = int(input())
list1 = []
for i in range(m):
    k,t = map(int,input().split())
    score = []
    for j in range(k):
        score.append([int(x) for x in input().split()])
    list1.append([find_tot(k,score),t])

list1.sort(key =lambda x : (-x[0],x[1]))

if m == 1:
    print(list1[0][1])
else:
    for i in range(1,m):
        if round(list1[i][0],4) < round(list1[0][0],4):
            ok = i-1
            break
        else:
            ok = m-1

    out = ''
    for i in range(ok):
        out += str(list1[i][1]) +' '
    out += str(list1[ok][1])
    print(out)












