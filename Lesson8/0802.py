first = input()
second = input()
bulls = 0
cows = 0
for i in range(len(first)):
    if first[i] == second[i]:
        bulls += 1
    elif second[i] in first:
        cows += 1
print(bulls, cows)