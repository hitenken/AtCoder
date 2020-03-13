def solv(t):
    c = 0
    while t % 100 == 0:
        t /= 100
        c += 1
    return c

D, N = map(int, input().split())
t = 1
c = 0
while c < N:
    n = solv(t)
    if n == D:
        c += 1
    t += 1

print(t -1)