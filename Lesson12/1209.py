symbup = input().upper()
symblow = input().lower()
phrase = input().split()
words = []
for word in phrase:
    if symbup in word or symblow in word:
        words.append(word)
for i in words:
    print(i)