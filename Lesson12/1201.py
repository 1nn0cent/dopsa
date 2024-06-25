N = int(input())
list = []
for i in range(N):
    word = input()
    if 'кот' in word:
        print(i + 1, word.find('кот')+1)
        