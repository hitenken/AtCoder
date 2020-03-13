N = int(input())
ans = 0
for i in range(N):
    x, u = map(str,input().split())
    if u == "BTC":
        ans += 380000.0 * float(x)
        continue
    ans += int(x)

print(ans)