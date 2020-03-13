from math import ceil
N, K = map(int, input().split())
P = list(map(int, input().split()))
E = [0]
E.append(sum([i for i in range(1, P[0] + 1)])/P[0])
for i in range(1,N):
    p = P[i]
    E.append(E[i] + ((1+p) / 2))
r = K
ans = 0
while r < N + 1:
    ans = max(ans, E[r] - E[r - K])
    r += 1
print(ans)