def count_ways_to_top(N):
    if N <= 2:
        return N
    if N == 3:
        return 4
    ways = [0]*(N+1)
    ways[1] = 1
    ways[2] = 2
    ways[3] = 4
    for i in range(4,N+1):
        ways[i] = (ways[i-1] + ways[i-2] + ways[i-3]) % 10000
    return ways[N]
N = int(input())
print(count_ways_to_top(N))
