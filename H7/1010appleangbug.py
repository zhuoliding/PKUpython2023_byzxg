n = int(input())
x = int(input())
y = int(input())
if y%x == 0:
    print(int(n-y/x))
else:
    print(int(n-1-y//x))