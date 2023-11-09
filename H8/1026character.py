string = input().upper()
dic = {}
for i in string:
    if i.isalpha():
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

max_count = max(dic.values())
list1 = []
for key,value in dic.items():
    if value == max_count:
        list1.append(key)
max_letter = min(list1) 
print(max_letter,max_count)