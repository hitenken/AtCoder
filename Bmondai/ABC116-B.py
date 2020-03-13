def check(s,i):
    if s in l:
        return i
    if s % 2 == 0:
        l.append(s)
        ans = check(s//2, i+1)
    else:
        l.append(s)
        ans = check(3 * s + 1, i + 1)
    return ans
s = int(input())
l = [s]
ans = 0
if s % 2 == 0:
    ans = check(s//2,2)
else:
    ans = check(3 * s + 1,2)
print(ans)