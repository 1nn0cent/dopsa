url = input()
key = input()

get = url.split('?')[1]

output = {}

for requset in get.split('&'):
    keys = requset.split('=')
    output[keys[0]] = keys[1]

if key in output:
    print(output[key])
