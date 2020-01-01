N = int(input())
s = [input() for i in range(N)]
num = 0
d = {}
for i in range(N):
    if ''.join(sorted(s[i])) in d:
        d[''.join(sorted(s[i]))] += 1
        num += d[''.join(sorted(s[i]))]
    else:
        d[''.join(sorted(s[i]))] = 0

print(num)