list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))
for i in range(len(list1)):
    list1[i] = (list1[i] + 5) % 10
for i in range(len(list2)):
    list2[i] = (list2[i] + 5) % 10

str1 = ''
str2 = ''
for x in list1:
    str1 += str(x) + ' '
for x in list2:
    str2 += str(x) + ' '
print(str1.strip(' '))
print(str2.strip(' '))