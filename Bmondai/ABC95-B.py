N, X = map(int, input().split())
m = [int(int(input())) for i in range(N)]
X = X - sum(m)
print(X//min(m) + N)