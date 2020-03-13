N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
minimum = 10**5
ans = 0
for i in range(N):
    if minimum > abs(A - (T-H[i] * 0.006)):
        minimum = abs(A - (T-H[i] * 0.006))
        ans = i+1
print(ans)