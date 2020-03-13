#ナップザック問題
#デバックすると動きが解る

def chmax(a, b):
    if b > a:
        a = b
    return a


N = int(input())
W = int(input())  #最大積載量

value = [int(i) for i in input().split()]
weight = [int(i) for i in input().split()]

dp = [[0 for i in range(W + 1)] for j in range(N + 1)]

for i in range(N):
    for j in range(W+1):
        if j >= weight[i]:#今現在の最大積載量(0~W)がweight[i]以下なら
            dp[i + 1][j] = chmax(dp[i][j], dp[i][j - weight[i]] + value[i])
        else:
            dp[i + 1][j] = dp[i][j]

print(dp[N][W])
