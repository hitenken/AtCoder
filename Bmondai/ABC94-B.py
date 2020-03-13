N, M, X = map(int, input().split())
A = list(map(int, input().split()))
l = 0
while A[l] <= X:
    l += 1
print(min(len(A[:l]), len(A[l:])))