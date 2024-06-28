def find_mountain(heightsMap):
    row = -1
    abs = 0
    for i in heightsMap:
        if max(i) > abs:
            abs = max(i)
    for i in heightsMap:
        row += 1
        column = -1
        for j in i:
            column += 1
            if j == abs:
                return row, column
