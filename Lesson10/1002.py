N = int(input())
good = []
all = []
for _ in range(N):
    student = input()
    if '5' in student or '4' in student:
        good.append(student)
        all.append(student)
    else:
        all.append(student)
for i in range(len(all)):
    print(all[i])
print()
for i in range(len(good)):
    print(good[i])