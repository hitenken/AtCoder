N, M = map(int, input().split())

bs = [True for i in range(N+1)]
for i in range(M):
    a = int(input())
    bs[a] = False

dp = [0 for i in range(N+1)]
dp[0] = 1
if bs[1] != False: dp[1] = 1

for i in range(2,N+1):
    if bs[i-1] != False:
        dp[i] += dp[i - 1]
    if bs[i - 2] != False:
        dp[i] += dp[i - 2]

print(dp[N] % 1000000007)