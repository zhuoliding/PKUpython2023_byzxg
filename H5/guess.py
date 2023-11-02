import random

secret = random.randint(1,100)
print(
    """猜数游戏！
我想了一个1-100的整数，你最多可以猜6次，
看看能猜出来吗"""
)
tries = 1
while tries <= 6:
    guess = int(input(f"1-100的整数，第{tries}次猜，请输入： "))
    if guess == secret:
        print(f'恭喜答对了！你只猜了{tries}次！\n就是这个： {secret}! ')
        break
    elif guess > secret:
        print('不好意思，你的数大了一点儿！ ')
    else:
        print('真遗憾，你的数小了一点儿！ ')
    tries += 1
else:
    print("哎呀！怎么也没猜中！再见！ ") 