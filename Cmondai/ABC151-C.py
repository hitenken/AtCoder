N, M = map(int, input().split())
ans = {}
ac = 0
wa = 0
flag = False
for i in range(M):
    p, s = input().split()
    if p not in ans:
        if s == "AC":
            ans[p] = []
            ans[p].append("AC")
        else:
            ans[p] = []
            ans[p].append("WA")
    else:
            if s == "WA":
                ans[p].append("WA")
            elif s == "AC":
                ans[p].append("AC")
for val in ans.values():
    count = 0
    for i in val:
        if flag != True:
            if i == "WA":
                count += 1
            if i == "AC":
                ac += 1
                wa += count
                flag = True
    flag = False
print(ac, wa)

