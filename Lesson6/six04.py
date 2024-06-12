M = int(input())
N = int(input())
K = int(input())
student = set()
unique = set()
for _ in range(M+N+K):
    surname = input()
    if surname not in student:
        student.add(surname)
    elif surname not in unique:
        unique.add(surname)
    else:
        unique.remove(surname)
count = len(student)-len(unique)
if len(unique)>0:
    print(len(unique))
    
else:
    print('NO')

