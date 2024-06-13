n = int(input())
words = []
for _ in range(n):
    word = input()
    words.append(word)
words.sort()

for i in range(n - 1):
    for j in range(n - 1 - i):
        if len(words[j]) > len(words[j + 1]):
            words[j], words[j + 1] = words[j + 1], words[j]
            
for i in words:
    print(i)