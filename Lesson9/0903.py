n = int(input())
phrase = []
for _ in range(n):
    word = input()
    phrase.append(word)
number = int(input())
result=""
for i in phrase:
    if len(i) >= number:
        result += i[number - 1]
print(result)