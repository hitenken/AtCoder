N, K, M = map(int, input().split())

A = list(map(int, input().split()))
avg = N * M
c = 0
for i in A:
    c += i

ans = avg - c
if ans > K:
    print(-1)
    exit()
if ans < 0:
    print(0)
    exit()
print(ans)
