N = int(input())
S = list(map(str, input().split()))
flag = False
for i in S:
    if i == 'Y':
        flag = True
print('Four' if flag else 'Three')
