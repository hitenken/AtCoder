N, K = map(int, input().split())
h = [int(input()) for i in range(N)]
h.sort()
mini = 10**10
for i in range(N - K + 1):
    mini = min(mini, h[i+K-1] - h[i])
print(mini)