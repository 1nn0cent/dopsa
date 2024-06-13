N = int(input())
list = []
for _ in range(N):
    phrase = input()
    list.append(phrase)
for phrase in list:
    if phrase[:3] == "Не " or phrase[:3] == "не ":
        print(phrase[3:])
    else:
        print(phrase)
        