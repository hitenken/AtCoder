N = int(input())
S = [input() for i in range(N)]
ans = {}

for s in S:
    if s not in ans:
        ans[s] = 1
    else:
        ans[s] += 1

n = max(ans.values())
l = []
for k, v in ans.items():
    if v== n:
        l.append(k)
l.sort()
for i in l:
    print(i)
