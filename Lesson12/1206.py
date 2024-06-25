line = input().upper().replace('', '-').split()
for i in range(len(line)):
    print(line[i][1:-1], end =' ')