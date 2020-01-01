N = int(input())
H = list(map(int, input().split()))
ans = 0
c = 0
H.reverse()

for i in range(1, len(H)):
    if H[i] >= H[i - 1]:
        c += 1
    else:
        c = 0
    ans = max(c, ans)

print(ans)