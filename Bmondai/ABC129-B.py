N = int(input())
W = list(map(int, input().split()))

mi_n = 100000
index = 0
for i in range(1,N):
    S1 = sum(W[0 : i])
    S2 = sum(W[i: N])
    if abs(S1 - S2) <= mi_n:
        mi_n = abs(S1 - S2)

print(mi_n)