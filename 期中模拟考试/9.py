[n,m] = list(map(int,input().split()))
arr1 = list(map(int,input().split()))
arr2 = [int(x) for x in input().split()]
arr1_in = [x for x in arr1 if x in arr2]
arr1_out = [x for x in arr1 if x not in arr2]
str1 = ''
for x in arr2:
    for y in arr1:
        if x == y:
            str1 += str(x) + ' '
arr1_out.sort()
for x in arr1_out:
    str1 += str(x) + ' '
print(str1.strip())