time = int(input())
if time < 0:
    print('Пуск')
else:
    
    for i in range(time, -1, -1):
        if i == 0:
            print('Пуск')
        else:
            print('Осталось секунд:',i)
