bd = {
    'янв': [],
    'фев': [],
    'мар': [],
    'апр': [],
    'май': [],
    'июн': [],
    'июл': [],
    'авг': [],
    'сен': [],
    'окт': [],
    'ноя': [],
    'дек': [],
}
output = []
for i in range(int(input())):
    data = input().split()
    name = data[0]
    month = data[2]
    bd[month].append(name)
    bd[month].sort()
for _ in range(int(input())):
    person = input()
    output.append(' '.join(bd[person]))
for x in output:
    print(x)