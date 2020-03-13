A, B, X = map(int, input().split())

def f(n):
    return A * n + B * len(str(n))

if A > X or B > X:
    print(0)

else:
    r = 10 ** 9 + 1
    l = 0
    while r - l > 1:
        c = (r + l) // 2
        if f(c) <= X:
            l = c
        else:
            r = c
    print(l)