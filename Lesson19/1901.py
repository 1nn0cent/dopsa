from operator import *
def arithmetic_operation(operation):
    oper = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': truediv
    }
    return oper[operation]
