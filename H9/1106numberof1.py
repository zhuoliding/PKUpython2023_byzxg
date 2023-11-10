n = int(input())
number = 0
for i in range(1,n+1):
    string = str(i)
    number += string.count('1')
print(number)



