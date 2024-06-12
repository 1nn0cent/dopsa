M = int(input())
N = int(input())
english = set()
german = set()

for _ in range(M):
   english.add(input())
for _ in range(N):
    german.add(input())
single = len(english.symmetric_difference(german))   

if single > 0:
    print(single)
else:
    print('NO')