S = input()

ans = 0
count = 0
for s in S:
    if s in ['A', 'C', 'G', 'T']:
        count += 1
        continue
    ans = max(ans, count)
    count = 0
ans = max(ans, count)
print(ans)