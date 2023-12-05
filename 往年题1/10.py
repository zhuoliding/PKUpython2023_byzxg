n,m = map(int,input().split())
list1 = list(map(int,input().split()))
a = sum(list1)
if a < m:
    print(0)
else:
    def total_choice(n,list1):
        global c
