[V,n] = list(map(int,input().split()))
vol = list(map(int,input().split()))
def find(n,list):
    if n == 1:
        return list[0]
    elif n > 1:
        V_max = 0
        for i in range(n):
            c = find(n-1,list[:i]+list[i+1:]) + list[i]
            d = c - list[i]
            if c >= V_max:
                if c <= V:
                    V_max = c
                if c > V:
                    if d >= V_max and d <= V:
                        V_max = d       
        return V_max
print(V-find(n,vol))
             