N = int(input())
P = list(map(int, input().split()))
minimum = P[0]
ans = 1
for i in range(1,N):
    if P[i] <= minimum:
        ans += 1
        minimum = P[i]
print(ans)