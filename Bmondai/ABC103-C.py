S = input()
T = input()

for i in range(len(S)):
    k = []
    for j in range(len(S)):
        if j == 0:
            k.append(S[-1])
            continue
        k.append(S[j - 1])
    S = k
    if "".join(S) == T:
        print("Yes")
        exit()
print("No")