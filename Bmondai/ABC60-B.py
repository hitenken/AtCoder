def GCD(x, y):
    if y == 0:
        return x
    return GCD(y, x % y)

A, B, C = map(int, input().split())
if B > A:
    A, B = B, A
gcd = GCD(A, B)

if C % gcd == 0:
    print("YES")
else:
    print("NO")