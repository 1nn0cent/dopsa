n = int(input())
search = []
found = []
keys = []
for _ in range(n):
    request = input()
    search.append(request)
    
nkey = int(input())
for _ in range(nkey):
    key = input()
    keys.append(key)

for request in search:
        if all(sites in request for sites in keys):
            print(request)

