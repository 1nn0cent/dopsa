n = int(input())
search = []
found = []

for _ in range(n):
    request = input()
    search.append(request)
    
key = input()
for request in search:
    if key in request:
        found.append(request)

for i in found:
    print(i)