def kakuritu(N, n, K):
    t = 1
    count = 0
    while N * t < K:
        t = t * 2
        count += 1
    return count

N, K = map(int, input().split())

n = 1
ans = 0
for i in range(1,N+1):
    ans += (1 / N) * ((1/2)**kakuritu(i, n, K))
    n += 1

print(ans)