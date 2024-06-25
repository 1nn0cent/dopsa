n = int(input().split('#')[1])
a = [input() for i in range(n)]
b = []
for i in a:
    if '#' in i:
        b.append(i[:i.find("#")].strip())
    else:
        b.append(i.strip())
for i in b:
    print(i)