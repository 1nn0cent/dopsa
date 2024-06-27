def space_game():
    c = 0
    for i in input():
        if i == " ":
            c += 1
    if c % 2 == 0:
        print("Вы выиграли")
    else:
        print("Вы проиграли")
 
