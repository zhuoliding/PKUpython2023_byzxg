w = list(map(int,input().split()))
M = w.pop(-1)
list1 = []
w.sort(reverse = True)
for i in range(2**len(w)):
    b_lis = [w[j] for j in range(len(w)) if (i>>j) & 1]
    if sum(b_lis) == M:
        str1 = ''
        for i in range(len(b_lis)-1,0,-1):
            str1 += str(b_lis[i]) + ','
        str1 += str(b_lis[0])
        list1.append(str1)
if list1 == []:
    print('NULL')
else:
    for i in range(len(list1)-1,-1,-1):
        print(list1[i])




