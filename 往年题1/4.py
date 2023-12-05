n = input()
m = input()
p = input()
q = input()
u = min(len(n),len(m),len(p),len(q))
for i in range(u):
    if n[i] == m[i] == p[i] == q[i]:
        a = i
    else:
        k = i
        break
else:
    k = u
if k != 0:
    print(n[:k])
