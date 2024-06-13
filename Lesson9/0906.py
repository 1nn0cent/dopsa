n = int(input())
numbers = []
sums = []
for _ in range(n):
    num = int(input())
    numbers.append(num)
for i in range(n-1):
    sum = numbers[i] + numbers[i+1]
    sums.append(sum)
for sum in sums:
    print(sum)
