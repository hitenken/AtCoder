N, D = map(int, input().split())
X = [[int(i) for i in input().split()] for j in range(N)]
count = 0
for i in range(N):
    for j in range(i+1,N):
        x = [0 for i in range(D)]  
        for k in range(D):
            x[k] = (X[i][k] - X[j][k]) ** 2
        d = sum(x) ** (1/2)
        if d == int(d): #整数判定
            count += 1

print(count)