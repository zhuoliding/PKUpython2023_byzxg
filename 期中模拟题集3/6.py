import math
n = int(input())
list1 = []
for i in range(2,int(2*math.sqrt(n))):
    for j in range(1,int(n//i)+1):
        c = 0
        for k in range(i):
            c += (j+k)
        if c == n:
            list1.append([i,j])
if list1 == []:
    print('None')
else:
    for i in range(len(list1)):
        str1 = ''
        for j in range(list1[i][0]-1):
            str1 += str(list1[i][1]+j) + '+'
        str1 += str(list1[i][1] + list1[i][0]-1) + '='
        str1 += str(n)
        print(str1)

















