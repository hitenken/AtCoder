N = int(input())
ans = 0
for i in range(N + 1):
    if i % 2 == 0:
        continue
    c = 0
    for j in range(1, i + 1):
        if i % j == 0:
            c += 1
    if c == 8:
        ans += 1
print(ans)