vol = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
word = input()
new = ''
c = vol.index(word[-1])
if c >= 12:
    u = c-12
else:
    u = 26-(12-c)
for i in range(len(word)):
    q = vol.index(word[i])
    new += vol[q-u]
print(new)


