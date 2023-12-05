n = int(input())
score = []
data = []
for i in range(n):
    data.append(list(map(int,input().split())))
for x in data:
    a = max(x)
    b = min(x)
    tot = (sum(x)-a-b)
    score.append(tot)
score_max = max(score)
inde = score.index(score_max)
print(inde+1,score_max)



