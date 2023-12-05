n = input()
c = str(int(n)*int(n))
if c[-len(n):] == n:
    print('yes')
else:
    print('no')

