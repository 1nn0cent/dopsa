short = ""
long = ""
words = []

while True:
    word = input()
    if word == "стоп":
        break
    words.append(word)
    if short == "" or len(word) < len(short):
        shor = word
    if long == "" or len(word) > len(long):
        long = word

if all(char in long for char in short):
    print("ДА")
else:
    print("НЕТ")