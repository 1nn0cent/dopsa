print('Вы много зарабатываете?')
first = input()
print('Вы счастливы?')
second = input()
if (first and second == 'да'):
    print('Вы счастливый и богатый')
elif (first == 'да' and second == 'нет'):
    print('Вы богатый, но счастья в деньгах нет')
elif (first == 'нет' and second == 'да'):
    print('Вы не богаты, но ведь не в деньгах счастье!')
elif (first and second == 'нет'):
    print('Однажды вы станете богатым и счастливым!')
else:
    print('Отвечайте на вопросы "да" или "нет"')
