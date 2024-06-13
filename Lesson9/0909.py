n = int(input())
before = []
after = []
for _ in range(n):
    money = int(input())
    before.append(money)
    after.append(money)
for i in range(n):
    after[i] = after[i]*3
for i in range(n):
    print(before[i])
print()
for i in range(n):
    print(after[i])