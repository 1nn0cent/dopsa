n = int(input())
full = []
short = []
for _ in range(n): 
    slogan = input()
    full.append(slogan)
    
parts = int(input())
for _ in range(parts):
    number = int(input())
    short.append(full[number - 1])

for i in short:
    print(i)
    