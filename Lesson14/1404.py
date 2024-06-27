def who_are_you_and_hello():
    while True:
        name = input('Введите ваше имя: ')
        if name.isalpha() and name[0].istitle() and name[1:].islower():
            print(f'Привет, {name}')
    