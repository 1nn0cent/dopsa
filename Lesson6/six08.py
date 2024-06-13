N = int(input())
surnames = set()
same_surname = set()
count = 0
for _ in range(N):
    surname = input()
    if surname not in surnames:
        surnames.add(surname)
    else:
        count += 1
        if surname not in same_surname:
            same_surname.add(surname)
count += len(same_surname)
print(count)