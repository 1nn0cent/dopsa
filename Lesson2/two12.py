phrase = input()
lenght = len(phrase)
cost = lenght * 40
cop = cost % 100
rub = cost // 100
print(rub, "р.", cop, "коп.")