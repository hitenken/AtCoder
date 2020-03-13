N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
fenum = sum(A)

if B[0] >= A[0]:
    B[0] -= A[0]
    A[0] = 0
    if B[0] > A[1]:
        A[1] = 0
    else:
        A[1] -= B[0]
        B[0] = 0
    
else:
    A[0] -= B[0] 
    B[0] = 0
    
for i in range(1, N):
    if B[i] >= A[i]:
        B[i] -= A[i]
        A[i] = 0
        if B[i] > A[i + 1]:
            A[i + 1] = 0
            continue
        A[i + 1] -= B[i]
        B[i] = 0
    
    else:
        A[i] -= B[i]
        B[i] = 0

print(fenum - sum(A))
