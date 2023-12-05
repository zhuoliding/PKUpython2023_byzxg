list_num = list(map(int,input().split()))
list1 = []
list2 = []
for x in list_num:
    if x % 2 == 0:
        list2.append(x)
    else:
        list1.append(x)
list1.sort(reverse = True)
list2.sort()
str1 = ''
for x in list1:
    str1 += str(x)+' '
for x in list2:
    str1 += str(x)+' '
print(str1.strip(' '))