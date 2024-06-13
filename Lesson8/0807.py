N = int(input())
words = []
num = []

for i in range(N):
    word = input()
    if 'кот' in word: 
        index = word.index('кот')+1
        num.append((i+1,index))
        
for m,k in num:
    print(m,k)