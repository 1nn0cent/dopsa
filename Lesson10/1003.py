N = int(input())
words = []
for _ in range(N):
    word = input()
    words.append(word)
words.sort()
for i in range(N):
    print(words[i])