line_number = 0
found_kot = False

while True:
    line = input()  
    line_number += 1 
    if 'Кот' in line or 'кот' in line:  
        found_kot = True
    if found_kot == True:  
        print(line_number)
        break
    if line == 'СТОП':
        print(-1)
        break