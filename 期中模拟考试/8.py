m = int(input())
wait = list(map(float,input().split()))
n = int(input())
time = list(map(float,input().split()))
for i in range(n):
    c = min(wait)
    d = wait.index(c)
    wait[d] += time[0]
    time.pop(0)
result = min(wait)
print(f'{result:.1f}')


