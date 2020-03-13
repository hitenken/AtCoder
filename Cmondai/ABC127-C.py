N, M = map(int, input().split())
idcard = [[int(j) for j in input().split()] for i in range(M)]

L = 0
R = 10**10
for i in idcard:
    L = max(L, i[0])
    R = min(R, i[1])
if R >= L:
    print(R - L + 1)
else:
    print(0)