N = int(input())
S = input()
i = 0
ans = 0
while i < N-2:
    if S[i] == 'A' and S[i + 1] == 'B' and S[i + 2] == 'C':
        ans += 1
    i += 1
print(ans)
        