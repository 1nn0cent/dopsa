word = input()
number = int(input())
if 1 <= number <= len(word):
    letter = word[number - 1]
    print(letter)
else:
    print('ОШИБКА') 