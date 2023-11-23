n = int(input())
volumn = list(map(int,input().split()))
def time(lis):
    if lis == []:
        return 0
    if 0 in lis:
        if lis[0] == 0:
            return time(lis[1:])
        elif lis[-1] == 0:
            return time(lis[:-1])
        else:
            for i in range(1,len(lis)-1):
                if lis[i] == 0:
                    return time(lis[:i]) +time(lis[i+1:])
    else:
        c = min(lis)
        lis = [x-c for x in lis]
        return time(lis) + c
            
print(time(volumn))      
