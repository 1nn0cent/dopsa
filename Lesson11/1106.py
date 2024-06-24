N = int(input())
list = []
for _ in range(N):
    recipe = input()
    if "лук" not in recipe:
        list.append(recipe)
print(', '.join(list))
