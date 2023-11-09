date = input().split()
y = int(date[0])
m = int(date[1])
d = int(date[2])
out = 'NO'
if m in [1,3,5,7,8,10,12]:
    if d > 0 and d < 32:
        out = 'YES'
elif m in [4,6,9,11]:
    if d >0 and d <31:
        out = 'YES'
elif m == 2:
    if d > 0 and d < 29:
        out = 'YES'
    elif (y%4 == 0 and y%100 != 0) or y%400 == 0:
        if d == 29:
            out = 'YES'
print(out)









