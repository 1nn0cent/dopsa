num = int(input())
divs = []
for i in range(1, num+1):
    if num % i == 0:
       divs.append(i)

for i in divs:
    print(i, end=' ') 
    
print()  
if len(divs) == 2:
    
    print('ПРОСТОЕ')
    
else:
    print('НЕТ')