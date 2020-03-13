N = int(input())
h = list(map(int, input().split()))
ans = 0

for l in range(N):
    while h[l] != 0:
        r = l+1
        for i in range(r, N):
            if h[i] == 0:
                break
            r += 1
        for i in range(l, r):
            h[i] -= 1
        ans += 1
print(ans)