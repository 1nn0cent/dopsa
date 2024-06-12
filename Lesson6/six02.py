n = int(input())
cities = set()
for i in range(n):
    city = input()
    cities.add(city)
if city in cities:
    print("TRY ANOTHER")
else:
    print('OK')

    
    