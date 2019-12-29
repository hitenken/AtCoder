N = int(input())
SP = [[str(i) for i in input().split()]for j in range(N)]
for i in range(N):
    SP[i][1] = int(SP[i][1])

DP = sorted(SP, key=lambda x: (x[0], -x[1]), reverse=False)
for j in DP:
    for c, i in enumerate(SP):
        if i == j:
            print(c+1)