S = input()
N = len(S)
for i in range(1,N+1):
    if i % 2 == 0:
        if S[i-1] not in ['L','U','D']:
            print('No')
            exit()
    else:
        if S[i-1] not in ['R', 'U', 'D' ]:
            print('No')
            exit()

print('Yes')