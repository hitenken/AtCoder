N = int(input())
s = input()
numE = s.count("E")
numW = 0
ans = 10**10
for i in range(N):
    if s[i] == 'W':
        ans = min(ans, numE + numW)
        numW += 1
    else:
        numE -= 1
        ans= min(ans, numE+numW)

print(ans)
