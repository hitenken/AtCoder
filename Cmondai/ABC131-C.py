def gcd(x,y):
    if y == 0:
        return x
    return gcd(y, x % y)

A, B, C, D = map(int, input().split())
lcm = (C * D) // gcd(C, D)
bsum = B - (B//C) - (B//D) + (B//lcm)
asum = (A - 1) - ((A - 1) // C) - ((A - 1) // D) + ((A - 1) // lcm)

print(bsum-asum)