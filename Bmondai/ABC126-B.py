S = input()

if (1 <= int(S[:2]) <= 12) and (1 <= int(S[2:4]) <= 12):
    print('AMBIGUOUS')
elif (0 <= int(S[:2]) <= 99) and (1 <= int(S[2:4]) <= 12):
    print('YYMM')
elif (1 <= int(S[:2]) <= 12) and (0 <= int(S[2:4]) <= 99):
    print('MMYY')
else:
    print('NA')