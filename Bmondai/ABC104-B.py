S = input()
if S[0] != 'A':
    print("WA")
elif ord(S[1]) < 97:
    print('WA')
elif ord(S[-1]) < 97:
    print("WA")
else:
    cnt = 0
    for i in range(1, len(S)-1):
        if S[i] == 'C':
            cnt += 1
    if cnt == 1:
        print("AC")
    else:
        print("WA")