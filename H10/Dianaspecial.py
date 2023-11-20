N = int(input())
room = []
for i in range(N):
    room.append(list(map(int,input().split())))
ans =[[0]*N for _ in range(N)]
#print(ans)
def value(a,b,ans):
    if ans[a-1][b-1] != 0:
        return ans[a-1][b-1]
    elif a == 1:
        ans[a-1][b-1] = sum(room[0][:b])
        return ans[a-1][b-1]
    elif b == 1:
        sum1 = 0
        for i in range(a):
            sum1 += room[i][0]
        ans[a-1][b-1] = sum1
        return ans[a-1][b-1]

    elif a > 1 and b > 1: 
        ans[a-1][b-1] = room[a-1][b-1] + max(value(a-1,b,ans),value(a,b-1,ans)) 
        return ans[a-1][b-1]
print(value(N,N,ans))
        

#非常好的一道题，核心在于减少内存占用。如果不用ans这个额外的列表的话，每算一步都会生成一个新的列表，导致内存占用过大。我们使用ans这个列表记录算过的值，从而避免重复计算。使用时，要注意
#1，在函数变量中加入ans
#2，当ans已被赋值时，直接return ans的值。

    