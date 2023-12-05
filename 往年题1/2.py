n = int(input())
height = list(map(int,input().split()))
h_min = int(input())
num = 0
for x in height:
    if x <= h_min:
        num += 1
print(num)