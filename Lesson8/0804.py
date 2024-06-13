size = int(input())

for row in range(size, 0 , -1):  
    table = ""
    for col in range(1, size + 1):
        letter = chr(64 + col)  
        table += f"{letter}{row} "

    print(table)