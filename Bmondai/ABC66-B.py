S = input()
leng = len(S)
ans = 1
for i in range(leng-1, 0, -1):
    if S[:(i // 2)] == S[i // 2:i]:
        ans = max(i, ans)
print(ans)
