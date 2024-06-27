d = {}
output = []
for _ in range(int(input())):
    x = input()
    word = x.split()
    d[word[0]] = x[len(word[0]) + 1:]
 
for _ in range(int(input())):
    word = input()
    if word not in d:
        output.append('Нет в словаре')
    else:
        output.append((d[word]))
for x in output:
    print(x)
