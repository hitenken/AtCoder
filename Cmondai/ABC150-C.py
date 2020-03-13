import itertools
N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
l = list(itertools.permutations(range(1,N+1)))
a = 0
b = 0
for n, val in enumerate(l):
    if list(val) == P:
        a = n+1
    if list(val) == Q:
        b = n+1
        if a != 0:
            break
print(abs(a-b))
            