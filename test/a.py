R, G, B, N = map(int, input().split())
ans = 0
for r in range((N//R)+1):
    for g in range((N//G)+1):
        v = R * r + G * g
        if v > N:
            break
        if (N - v) % B == 0:
            ans +=1 
        
print(ans)
