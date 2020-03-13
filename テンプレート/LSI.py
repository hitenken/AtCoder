#O(N^2)
def lsi():
    for i in range(1, N):
        for j in range(i):
            if L[i] > L[j]:
                dp[i] = max(dp[i], dp[j] + 1)

if __name__ == "__main__":
    N = int(input())
    L = list(map(int, input().split()))
    dp = [1 for i in range(N)]
    lsi()
    ans = 0
    for i in range(N):
        ans = max(ans, dp[i])
    print(ans)