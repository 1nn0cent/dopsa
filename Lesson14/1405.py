def triangle():
    a = float(input())
    b = float(input())
    c = float(input())
    if (a + b <= c) or (a + c <= b) or (b + c <= a) or (c + a <= b):
        print('Это не треугольник')
    else:
        print('Это треугольник')


triangle()