def min_packs(w, n, snacks):
    snacks.sort(reverse=True)  # 按重量降序排序
    count = 0  # 记录使用的包装袋数量

    while snacks:
        current_weight = snacks.pop(0)  # 取出当前最重的零食
        count += 1  # 使用一个包装袋

        if snacks and current_weight + snacks[-1] <= w:
            snacks.pop()  # 如果当前零食和剩余零食重量小于等于w，放入同一包装袋

    return count

# 读取输入
w = int(input())
n = int(input())
snacks = list(map(int, input().split()))

# 调用函数并输出结果
result = min_packs(w, n, snacks)
print(result)