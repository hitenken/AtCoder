from math import factorial
mod = int(10**9 + 7)

'''
シンプルな実装
nCr = nPr/r!
'''
def cmb(n, r):
    comb1 = 1
    for i in range(r):
        comb1 = (comb1 * (n - i)) % mod
    comb2 = factorial(r) % mod  #階乗
    comb2 = pow(comb2, mod -2 , mod)
    return (comb1 * comb2) % mod

'''
nCr = n!/((n-r)! * r!)
'''
def cmb2(n, r):
    a = 1  # n!
    b = 1  # (n-r)!
    c = 1  # r!

    for i in range(n):
        a = (a * (n - i)) % mod
    for i in range(n-r):
        b = (b * (n - r - i)) % mod
    for i in range(r):
        c = (c * (r - i)) % mod
    bc = (b * c) % mod
    return (a // bc) % mod  


'''
累積和
フェルマーの小定理
繰り返し二乗法
を使用した実装
'''
def inv(x):
    res = 1
    k = mod - 2
    y = x
    #繰り返し二乗和
    while (k):
        if (k & 1 == 1):
             res = (res * y) % mod
        y = (y * y) % mod
        k //= 2
    return res

def cmb3(n, r):
    f = [1]
    for i in range(1, 101010):
        f.append((f[i - 1] * i) % mod)
    a = f[n]
    b = f[n - r]
    c = f[r]
    bc = (b * c) % mod

    return (a * inv(bc)) % mod
    
n, a = map(int, input().split())
print(cmb(n, a))