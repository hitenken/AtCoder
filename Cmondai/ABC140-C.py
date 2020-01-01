N = int(input())
B = [int(i) for i in input().split()]
A = B[0]
for i in range(1, N-1):
    A += min(B[i-1],B[i])
A += B[N-2]
print(A)