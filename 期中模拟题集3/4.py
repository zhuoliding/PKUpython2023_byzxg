n = input()
m = input()
if len(n) < len(m):
    print('BLUE')
elif len(n) > len(m):
    print('RED')
else:
    for i in range(len(n)):
        if n[i] > m[i]:
            print('RED')
            break
        elif n[i] < m[i]:
            print('BLUE')
            break
    else:
        print('EQUAL')
