print("Вы стоите в коридоре на развилке у трех проходов.")
print("Вы можете пойти 'налево', 'направо' или 'прямо'.")
print("Введите одно из слов в кавычках для выбора.")
way = input()
if way == 'налево':
    print("Вы вошли в ярко освещенную комнату, в которой находится стальная дверь и большое панорманое окно. Из двери доносится скрежет. Вам становится не по себе, у Вас есть выбор 'дверь' или 'окно'")
    room = input()
    if room == 'окно':
        print('Со страху вы выпрыгиваете в окно и ломаете обе ноги. Вам уже не сбежать.')
    if room == 'дверь':
        print('Дрожащими руками вы дергаете за ручку. Темную комнату озаряет свет и вы наконец видите причину скрежета - это пушистый котик!')
    else:
        print('Выбирайте одно из слов, написанных в кавычках. Ошибка!')
if way == 'прямо':
    print('Вы оказываетесь в столовой. Шикарный стол чуть ли не ломится от явств. На другом конце стола сидит бледный человек без глаз. Насмотревшись фильмов ужасов в детстве, вы теряеет сознание.') 
if way == 'направо':
    print('Решив, что правый ход - самый правильный, вы направляетесь туда. Как оказалось, справа вас ждала лишь верная смерть.') 
