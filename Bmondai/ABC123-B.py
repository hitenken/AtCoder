import itertools

A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

P = list(itertools.permutations([A, B, C,D,E]))
time = 0
mini = 10**3
for i in P:
    count = 0
    for j in i:
        time += j
        if (count ==4):
            break
        if j % 10 != 0:
            time += 10 - (time % 10)
        count += 1
    mini = min(mini, time)
    time = 0

print(mini)