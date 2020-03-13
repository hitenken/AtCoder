N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
max_x = max(x)
min_y = min(y)
flag = False
for Z in range(X + 1, Y + 1):
    if max_x < Z and min_y >= Z:
        flag = True
print('No War' if flag else 'War')