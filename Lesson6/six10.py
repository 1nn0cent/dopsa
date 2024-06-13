M = int(input())
menu = set()

for _ in range(M):
    dish = input()
    menu.add(dish)

N = int(input())
cooked = set()
for _ in range(N):
    num = int(input())
    for _ in range(num):
        dish = input()
        cooked.add(dish)
new = menu - cooked
for i in new:
    print(i)

