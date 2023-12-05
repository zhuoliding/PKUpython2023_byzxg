num = ['1','2','3','4','5','6','7','8','9','0']
stri = input()
inde = []
inde1 = []
for i in range(len(stri)):
    if stri[i] not in num:
        inde.append(i)
        inde1.append(stri[i])
valu = [int(stri[:inde[0]])]
for i in range(len(inde)-1):
    valu.append(int(stri[inde[i]+1:inde[i+1]]))
valu.append(int(stri[inde[-1]+1:]))
while '#' in inde1:
    i = inde1.index('#')
    d = valu[i]*valu[i+1] + valu[i] -valu[i+1]
    valu[i] = d
    valu.pop(i+1)
    inde1.pop(i)
sum = valu[0]
for i in range(len(inde1)):
    if inde1[i] == '+':
        sum += valu[i+1]
    else:
        sum -= valu[i+1]
print(sum)






