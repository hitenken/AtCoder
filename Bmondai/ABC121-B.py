N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = [[int(j) for j in input().split()] for i in range(N)]
ans = 0
for a in A:
    count = 0
    for i in range(M):
        count += a[i] * B[i]
    if count + C > 0:
        ans += 1
print(ans)