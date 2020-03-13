import itertools
N, K = map(int, input().split())
A = list(map(int, input().split()))

C = list(itertools.combinations(A, 2))
ans = []
for c in C:
    ans.append(c[0] * c[1])
ans.sort()
print(ans[K-1])