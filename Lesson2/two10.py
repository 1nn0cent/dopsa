a = float(input())
b = float(input())
c = input()

if c == '-':
    print(float(a-b))
elif c == '+':
    print(float(a+b))
elif c == '*':
    print(float(a*b))
elif c == '/':
    if b == 0:
        print(888888)
    else:
        print(float(a/b))
else:
    print(888888)