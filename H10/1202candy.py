N = int(input())
number = list(map(int,input().split()))
averge = sum(number)//N
#print(N,number,averge)
time = 0
averge1 = averge
for i in range(N-1):
    if number[i] > averge1:
        number[i+1] += number[i] - averge1
        time += 1
        averge1 = averge 
    elif number[i] < averge1:
        averge1 = averge + averge1 - number[i]
        time += 1
print(time)

