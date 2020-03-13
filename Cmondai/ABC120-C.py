S = input()

count1 = 0
count0 = 0

for i in S:
    if i == '1':
        count1 += 1
    else:
        count0 += 1

print(min(count0, count1) * 2)