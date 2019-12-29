N = int(input())
count = 0
for i in range(1, N + 1):
    i = str(i)
    if len(i) % 2 != 0:
        count += 1

print(count)