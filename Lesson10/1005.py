N = int(input())
names = []
for _ in range(N):
    names.append(input())
K = int(input())
M = int(input())
for _ in range(M):
    alive = []
    i = 1
    for name in names:
        if i % K != 0:
            alive.append(name)
        i += 1
    names = alive
    
for i in names:
    print(i)
