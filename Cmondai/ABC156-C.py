N = int(input())
X = list(map(int, input().split()))
ans = 10**10
for i in range(min(X), max(X) + 1):
    sum_ = 0
    for x in X:
        sum_ += (x - i)** 2
    ans = min(ans,sum_)
print(ans)
        