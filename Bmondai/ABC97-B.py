X = int(input())
ans = 1
i = 2
while i * i <= X:
    j = 1
    maxi = i
    while i ** j <= X:
        maxi = i ** j
        j += 1
    ans = max(ans, maxi)
    i += 1

print(ans)