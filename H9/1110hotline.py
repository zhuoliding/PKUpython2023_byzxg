m = int(input())
lin = list(map(float,input().split()))
n = int(input())
wait = list(map(float,input().split()))
t = 0
for i in range(0,n):
    a = min(lin)
    b = lin.index(a)
    t += a
    lin = [item - a for item in lin]
    lin[b] = wait[i]
t += min(lin)
print(f'{t:.1f}')


