N = input()
sum_ = sum(list(map(int, N)))
if int(N) % sum_ == 0:
    print('Yes')
else:
    print('No')