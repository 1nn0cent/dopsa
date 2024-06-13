max = int(input())
N = int(input())
list = []
for _ in range(N):
    phrase = input()
    list.append(phrase)
    
for phrase in list: 
       
    if len(phrase) <= max:
        print(phrase)
    else:
        short = phrase[:max - 3] + "..."
        print(short)