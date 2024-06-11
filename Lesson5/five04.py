n = int(input())
found = False
for i in range(n):
    phrase = input()
    if 'кот' in phrase or 'Кот' in phrase:
        found = True
        break
if found == True:
    print('МЯУ')
else:
    print('НЕТ')        