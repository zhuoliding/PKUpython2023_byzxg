data = input().split()
c = data[0]
d = int(data[1])
e = int(data[2])
if c == 'alpha':
    if 2 + d >= e:
        print('YES')
    else:
        print('NO')
if c == 'beta':
    if 1 + d >= e:
        print('YES')
    else:
        print('NO')
if c == 'gamma':
    if 3 + d >= e:
        print('YES')
    else:
        print('NO')
if c == 'delta':
    if 1 + d*5 >= e:
        print('YES')
    else:
        print('NO')
