import math

k = int(input())
list1 = []
for i in range(k):
    m = int(input())
    a = input()
    n = int(input())
    list1.append([m, a, n])
dict = {'0':0,'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,'9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
        'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27,
        'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': "35"}


def trans(m, a):
    c = 0
    for i in range(len(a)):
        c += dict[a[-i-1]] * (m ** i)
    return c


def get_key(dict, value):
    return [k for k, v in dict.items() if v == value]


def invers(n, a):
    k = int(math.log(a, n))
    str1 = ''
    for i in range(k, -1, -1):
        u = a // (n ** i)
        a = a % (n ** i)
        str1 += str(get_key(dict, u)[0])
    return str1


for i in range(k):
    a_10 = trans(list1[i][0], list1[i][1])
    print(invers(list1[i][2], a_10))
