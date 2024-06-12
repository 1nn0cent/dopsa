n = int(input())
found = False
for i in range(n):
    phrase = input()
    if 'кот' in phrase or 'Кот' in phrase:
        found = True
    if 'Пёс' in phrase or 'пёс' in phrase:
        found = False
if found == True:
    print('МЯУ')
else:
    print('НЕТ')        