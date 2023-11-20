w = int(input())
n = int(input())
weight = list(map(int,input().split()))
weight.sort()
def number(w1,n1,weights):
    if n1 == 1:
        return 1
    elif n1 == 0:
        return 0
    else: 
        if weights[n1-1] + weights[0] <= w1:
            weights.pop(0)
            weights.pop(-1)
            return number(w1,n1-2,weights)+1
        else:
            weights.pop(-1)
            return number(w1,n1-1,weights)+1
print(number(w,n,weight))