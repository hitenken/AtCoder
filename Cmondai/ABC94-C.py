N = int(input())
X = list(map(int, input().split()))
Y = sorted(X)
l = N // 2

for i in range(N):
    if X[i] < Y[l]:
        print(Y[l])
    else:
        print(Y[l- 1])