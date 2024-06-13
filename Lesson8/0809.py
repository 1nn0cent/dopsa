N = int(input())
lines = []

for _ in range(N):
    line = input()
    lines.append(line)
    
for line in lines:  
    if line[:4] == '####':
        continue      
    if line[:2] == '%%':
        print(line[2:])
    else:
        print(line)
