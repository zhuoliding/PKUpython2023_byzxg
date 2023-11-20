w1 = int(input())
n1 = int(input())
weight1 = list(map(int,input().split()))
weight1.sort()



def number(w,n,weight):
    count = 0
    while n >= 1:
        if n == 1:
            n = 0
            count += 1
        elif weight[n-1]+weight[0] <= w:
            weight.pop(-1)
            weight.pop(0)
            n = n - 2
            count += 1
        else:
            weight.pop(-1)
            n = n - 1
            count += 1
    return count
print(number(w1,n1,weight1))
    




