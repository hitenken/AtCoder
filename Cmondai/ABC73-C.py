N = int(input())
A = [int(input()) for i in range(N)]
l = {}

for a in A:
    if a not in l:
        l[a] = 0
    if l[a] != 0:
        l[a] = 0
    else:
        l[a] = 1

ans = 0
for d in l.values():
    ans += d

print(ans)