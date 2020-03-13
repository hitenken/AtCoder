W, H ,x, y = map(int, input().split())

print(W * H / 2, end=" ")
if 2 * x == W and 2 * y == H:
    print(1)
else:
    print(0)
    
