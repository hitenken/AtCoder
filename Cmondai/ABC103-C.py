def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

N = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
lcm = a[0]
for i in range(1, N):
    lcm =(lcm * a[i]) // gcd(lcm, a[i])
ans = 0
for i in a:
    ans += (lcm-1) % i
print(ans)