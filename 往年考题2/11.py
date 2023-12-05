n,k = map(int,input().split())
if n <= k:
    print(2)
else:
    a = n // k
    b = n % k
    c = (n+b)//k
    d = (n+b) %k
    if d == 0:
        print(a+c)
    else:
        print(a+c+1)
