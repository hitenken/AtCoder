N = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
alice = 0
bob = 0
for i in range(N):
    if i % 2 != 0:
        alice += a[i]
        continue
    bob += a[i]
print(bob - alice)
