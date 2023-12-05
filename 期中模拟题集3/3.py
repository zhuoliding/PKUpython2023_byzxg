n = input()
if int(n) > 0:
    j = ''
    for i in range(len(n)-1,-1,-1):
        j += n[i]
    j = j.strip('0')
    print(j)
elif int(n) == 0:
    print(0)
elif int(n) < 0:
    n = n[1:]
    j = ''
    for i in range(len(n) - 1, -1, -1):
        j += n[i]
    j = j.strip('0')
    print('-',j,sep = '')


