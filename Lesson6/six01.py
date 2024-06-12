first = []
second = []
while True:
    num = input()
    if num == "":
        break
    first.append(int(num))
while True:
    num = input()
    if num == "":
        break
    second.append(int(num))
same = set(first).intersection(second)
if same:
    for num in same:
        print(num)
else:
    print('EMPTY')