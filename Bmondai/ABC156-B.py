N, K = map(int, input().split())
i = 0
while N >= K ** i:
    i += 1
if i == 0:
    print(1)
    exit()
print(i)