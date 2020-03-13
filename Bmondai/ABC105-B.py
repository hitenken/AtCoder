N = int(input())
flag = False
for i in range((N // 4) + 1):
    for j in range((N // 7) + 1):
        if i * 4 + j * 7 == N:
            flag = True
print('Yes' if flag else 'No')