sum = 0
count = 0
first_count = 0
check = False
while True:
    a = int(input())
    sum += a
    count += 1
    if sum == 10:
        check = True
        first_count = count
    if a == 0:
        print(first_count)
        break 
