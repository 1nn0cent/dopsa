one = int(input())
two = int(input())
three = int(input())
heigth = [one, two, three]
heigth.sort(reverse=True)
for i in heigth:
    print(i)