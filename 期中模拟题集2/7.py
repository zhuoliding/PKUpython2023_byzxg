stri = input().lower()
n = 1
if len(stri) == 1:
    print('(%s,%s)' % (stri[0],1))
else:
    new = ''
    for i in range(1,len(stri)-1):
        if stri[i] == stri[i-1]:
            n += 1
        else:
            new += '(%s,%s)' % (stri[i-1],n)
            n = 1
    if stri[-2] == stri[-1]:
        new += '(%s,%s)' % (stri[-1],n+1)
    else:
        new += '(%s,%s)' % (stri[-2], n)
        new += '(%s,%s)' % (stri[-1], 1)
    print(new)





