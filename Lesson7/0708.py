num = int(input())
while num < 1000000000 and str(num)[0] != '1':
    num = num * int(str(num)[0])
print(num)