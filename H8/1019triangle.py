list = input().split(' ')
a = int(list[2])-int(list[0])
b = int(list[3])-int(list[1])
c = int(list[4])-int(list[0])
d = int(list[5])-int(list[1])
s = abs(1/2*(a*d-b*c))
if s == 0:
    print('Error')
else:
    print(f'{s:.4f}')