n = int(input())
war = "Евразия"
peace = "Остазия"
for i in range(n):
    report = input()
    if report == 'С кем война?':
        print(war)
    if report == 'С кем мир?':
        print(peace)
    if report == 'Меняем':
        war, peace = peace, war
        