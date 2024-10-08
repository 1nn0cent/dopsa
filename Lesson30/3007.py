class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients
    def __call__(self, x):
        return sum([self.coefficients[i]*x**i for i in range(len(self.coefficients))])
    def __add__(self, p):
        a = self.coefficients
        b = p.coefficients
        if len(a)<len(b):
            a += [0]*(len(b)-len(a))
        else:
            b += [0]*(len(a)-len(b))
        return Polynomial([a[i]+b[i] for i in range(len(a))])

