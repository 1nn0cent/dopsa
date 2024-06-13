first = input()
while True:
    second = input()
    if first[-1] != second[0]:
        print(second)
        break
    first = second