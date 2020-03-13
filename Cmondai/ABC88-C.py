C = [list(map(int, input().split())) for i in range(3)]
x = [0,0,0]
y = [0,0,0]
for i in range(3):
    y[i] = C[0][i] - x[0]
for i in range(3):
    x[i] = C[i][0] - y[0]
flag = True
for i in range(3):
    for j in range(3):
        if x[i] + y[j] != C[i][j]:
            flag = False
print('Yes' if flag else 'No')
