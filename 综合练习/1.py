a = int(input())
if a > 0:
    b = str(a).strip('0')
    c=''
    for i in range(len(b)-1,-1,-1):
        c += b[i]
    print(c)
elif a < 0:
    b = str(-a).strip('0')
    c = ''
    for i in range(len(b) - 1, -1, -1):
        c += b[i]
    print('-',c,sep='')
else:
    print('0')
