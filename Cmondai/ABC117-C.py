N, M = map(int, input().split())
X = list(map(int, input().split()))
if N >= M:
    print(0)
    exit()
X.sort()
leng = []
for i in range(1, M):
    leng.append(X[i] - X[i-1])
ans = sorted(leng, reverse = True)
print(sum(ans[N - 1:]))