name = input()
canbeused = "abcdefghijklmnopqrstuvwxyz0123456789_"

for char in name:
    if char not in canbeused:
        print('Неверный символ:',char)
        break
    else:
        print('OK')