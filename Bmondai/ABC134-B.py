N, D = map(int, input().split())
cnt = 0
while True:
    if N > 0:
        cnt += 1
        N -= 2 * D + 1
    else:
        break

print(cnt)