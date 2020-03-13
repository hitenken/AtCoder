N = int(input())
A = [int(input()) for i in range(N)]

x = A[:]
x.sort()
Amax = x[N-1]
Amax2 = x[N-2]
print("")
for a in A:
    if a < Amax:
        print(Amax)
    elif a == Amax:
        print(Amax2)