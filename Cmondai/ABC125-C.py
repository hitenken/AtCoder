def gcd(a, b):
    if b > a:
        tmp = a
        a = b
        b =tmp
    while b != 0:
        a, b = b, a % b
    return a

N = int(input())
A = list(map(int, input().split()))

L = [0 for i in range(N+1)]
for i in range(0,N):
    L[i + 1] = gcd(L[i], A[i])
    
R = [0 for i in range(N+1)]
for i in range(N,0,-1):
    R[i-1] = gcd(R[i],A[i-1]) 

ans = []
for i in range(1,N+1):
    ans.append(gcd(L[i - 1], R[i]))

print(max(ans))