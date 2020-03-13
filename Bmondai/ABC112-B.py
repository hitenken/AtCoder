N, T = map(int, input().split())
ans = []
for i in range(N):
    c, t = map(int, input().split())
    if t <= T:
        ans.append(c)
if not ans:
    print("TLE")
else:
    print(min(ans))