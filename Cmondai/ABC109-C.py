def gcd(x1, x2):
    if x2 == 0:
        return x1
    return gcd(x2, x1 % x2)

N, X = map(int, input().split())
x = list(map(int, input().split()))
if N == 1:
    print(abs(X - x[0]))
    exit()
x.sort()
D = gcd(abs(X-x[0]), abs(X-x[1]))
for i in range(2, N):
    D = gcd(D, abs(X - x[i]))
print(D)