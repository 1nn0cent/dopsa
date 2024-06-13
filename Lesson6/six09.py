M = int(input())
frigde = set()

for _ in range(M):
    product = input()
    frigde.add(product)
    
N = int(input())
recipes = set()

for _ in range(N):
    dish = input()
    count = int(input())
    ingredients = set()
    for _ in range(count):
        name = input()
        ingredients.add(name)
        
    if ingredients.issubset(frigde):
        recipes.add(dish)

for i in recipes:
    print(i)

    