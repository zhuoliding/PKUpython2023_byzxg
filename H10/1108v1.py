N = int(input())
number = list(map(int,input().split()))
T = int(input())
def match(n,list1):
    for i in range(n-1):
        if list1[n-1] + list1[i] == T:
            return [i,n-1]
    else:
        list1.pop(-1)
        return match(n-1,list1)

list2 = match(N,number)
print(list2[0],list2[1])
