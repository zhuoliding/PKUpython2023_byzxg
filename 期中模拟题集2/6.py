a = input()
b = input()
for i in range(len(a)):
    c = a[i]
    d = b.index(c)
    b = b[:d]+b[d+1:]
print(b)