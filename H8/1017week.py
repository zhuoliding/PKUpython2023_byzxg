li = input().split()
w = int(li[0])
m = int(li[1])
d = int(li[2])
#print(w,m,d,m//2)
if m == 1:
    day = (w+d-1)%7
elif m == 2:
    day = (w+d-1+31)%7
elif m%2 !=0 and m <=7:
    day = (w+d-3+m//2*61)%7
elif m%2 ==0 and m <=7:
    day = (w+d-3+(m//2)*61-30)%7
elif m%2 !=0 and m >=8:
    day = (w+d-2+m//2*61)%7
elif m%2 ==0 and m >=8:
    day = (w+d-3+(m//2)*61-30)%7
if day == 0:
    print(7)
else:
    print(day)



