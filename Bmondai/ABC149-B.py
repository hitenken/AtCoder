import math
A, B, K = map(int, input().split())

if A >= K:
    A = A - K
    print(A, end=" ")
    print(B)
    exit(0)

if K > A:
    K = K - A
    A = 0
    if K >= B:
        B = 0
        print(A, end=" ")
        print(B)
        exit(0)
    if B > K:
        B = B - K
        print(A, end=" ")
        print(B)
        exit(0)
    
'''
for i in range(K):
    if A >= 1:
        A -= 1
    elif B >= 1:
        B -= 1
    if A == 0 and B == 0:
        break

print(A, end=" ")
print(B)
'''