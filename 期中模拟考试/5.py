N = int(input())
form_1 = [input().split() for _ in range(N)]
form_1.sort(key=lambda x:float(x[1]))
form_2 = form_1[:10]
form_2.sort(key=lambda x:(-float(x[2]),float(x[1])))
for x in range(9):
    print(form_2[x][0],end=' ')
print(form_2[9][0])