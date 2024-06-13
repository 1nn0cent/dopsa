M = int(input())
list = []

for _ in range(M):
    group_num = int(input())
    students = set()
    for _ in range(group_num):
        surname = input()
        students.add(surname)
    list.append(students)  

unique = set(list[0])
for names in list[1:]:
    unique.intersection_update(names)
    
for name in unique:
    print(name)