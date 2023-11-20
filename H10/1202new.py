N = int(input())
num = list(map(int,input().split()))
averge = sum(num) // N
number = N
total = 0
for i in range(N):
    total += num[i]
    if total == averge*(i+1):
        number -= 1
print(number)



