lst = []
 
while True:
    try:
        lst.append(int(input()))
    except:
        break
 
if len(lst) == 0:
    print(-1)
else:
    print(sum(lst)/len(lst))