n = int(input('Please input size(3~20):'))
for i in range(n):
    line = " " * (n - 1 - i) + '@' * (2 * i + 1)
    print(line)
