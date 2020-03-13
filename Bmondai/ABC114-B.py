S = input()
L = []
ans = 10**5
for i in range(2, len(S)):
    L.append(S[i - 2] + S[i - 1] + S[i])
for l in L:
    ans = min(ans, abs(753 - int(l)))
print(ans)