N = int(input())
num = list(map(int,input().split()))
[L,R] = list(map(int,input().split()))
sum_L = 0
sum_R = 0
if sum(num) < L*N or sum(num) > R*N:
    print(-1)
else:
    for x in num:
        if x > R:
            sum_R += x - R
        elif x < L:
            sum_L += L -x
    print(max(sum_L,sum_R))
