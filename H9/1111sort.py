#题目描述
#一个班级有N名学生（10 <= N <= 100），每位学生包含姓名、年龄和成绩信息，请按照成绩由高到低输出年龄最小的10名学生的姓名。

#注意：假设名字不会超过32个字符，没有同年龄的情况。
#如果成绩相同，则按照年龄从小到大输出。

#关于输入
#输入N+1行，第一行是正整数N，之后每行包含学生姓名、年龄和成绩，中间用空格隔开。

#关于输出
#输出一行学生的姓名，中间用空格隔开。
N = int(input())
lin = []
for i in range(0,N):
    lin.append(input().split())
lin.sort(key=lambda x:(-int(x[1])),reverse = True)
lin1 = lin[:10]
lin1.sort(key=lambda x:(-float(x[2])))
for i in range(0,9):
    print(lin1[i][0],end=' ')
print(lin1[9][0])
#输入样例
#10
#Tom 18 90
#Jack 16 90
#Alice 15 100
#John 17 80
#Bob 18 60
#Lily 16 100
#Ann 17 90
#Mike 16 80
#Mary 16 100
#Jane 17 80


