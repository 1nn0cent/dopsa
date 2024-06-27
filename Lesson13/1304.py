n = int(input())
coord = []
for i in range(n):
    one, two = input().split()
    coord.append((int(one), int(two)))
result = []
while len(coord) > 0:
    good = []
    a = coord[0][0] // 10 * 10
    b = coord[0][1] // 10 * 10
    for i in range(0, len(coord)):
        x = coord[i][0] // 10 * 10
        y = coord[i][1] // 10 * 10
        if x == a and y == b:
            good.append(coord[i])
    result.append(good)
    coord = list(filter(lambda tochka: tochka not in good, coord))
    
count = [len(result[i]) for i in range(len(result))]
mcount = max(count)
print(mcount)

