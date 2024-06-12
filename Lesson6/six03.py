M = int(input())
N = int(input())
student = set()
unique = set()
for _ in range(M+N):
    surname = input()
    if surname not in student:
        student.add(surname)
    elif surname not in unique:
        unique.add(surname)
count = len(student)-len(unique)
if count == 0:
    print('NO')
else:
    print(count)

