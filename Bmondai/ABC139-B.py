A, B = map(int, input().split())
outlet = 1
ans = 0
while outlet < B:
    outlet -= 1
    outlet += A
    ans += 1
print(ans)