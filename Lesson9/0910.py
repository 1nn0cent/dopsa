n = int(input())
numbers = []
for _ in range(n):
    num = int(input())
    numbers.append(num)
p = int(input())
q = int(input())
sum = 0
i = 1

for num in numbers:
    if i >= p:
        sum += num
    if i == q:
        break
    i += 1
print(sum)