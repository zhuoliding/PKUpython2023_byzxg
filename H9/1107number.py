n = int(input())
sum = 0
for i in range(1,n+1):
    if i%7 != 0 and str(i).count('7') == 0:
        sum += i
print(sum)
     