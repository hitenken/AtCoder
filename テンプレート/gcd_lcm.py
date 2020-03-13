
#a>bとする
def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)


if __name__ == "__main__":
    q = list(map(int, input().split()))
    gcd = q[0]
    for i in range(1,len(q)):
        gcd = GCD(gcd, q[i])
    print(gcd)

    lcm = q[0]
    for i in range(1,len(q)):
        lcm = lcm * q[i] // GCD(max(lcm, q[i]), min(lcm, q[i]))
        
    print(lcm)

    '''
import fractions
a = list(map(int, input().split()))
ans = a[0]
for i in range(1, len(a)):
    ans = ans * a[i] // fractions.gcd(ans, a[i])
print(ans)
 '''