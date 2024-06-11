line_number = 0
found_kot = False
num = 0
firstnum = 0
while True:
    line = input()  
    line_number += 1 
    if 'Кот' in line or 'кот' in line:  
        found_kot = True
        num = line_number 
    if firstnum == 0:
        firstnum = num
    if line == 'СТОП' and found_kot == True:  
        print(firstnum)
        break
    if line == 'СТОП' and found_kot == False:
        print(-1)
        break

    