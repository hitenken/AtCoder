"""
n個の数列Aの部分列の合計がK以下となる部分列の長さの最小値
"""

n, k = map(int, input().split())
A = list(map(int, input().split()))

r = 0
ans = 10 ** 10
sum_ = 0
for l in range(n):
    while r < n and sum_ + A[r] < k:
        sum_ += A[r]
        r += 1
    
    ans = max(ans, r - l)
    sum_ -= A[l]
    if r == l:
        r += 1
    else:
        l += 1

print(ans)