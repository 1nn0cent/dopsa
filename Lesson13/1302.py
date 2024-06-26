dict = {}
for i in range(int(input())):
    num, name = input().split()
    if name in dict:
        dict[name].append(num)
    else:
        dict[name] = [num]

for i in range(int(input())):
    key = input()
    if name in dict:
        print(*dict[name])
    else:
        print('Нет в телефонной книге')
