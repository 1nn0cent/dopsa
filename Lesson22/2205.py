import random
import string

def generate_password(length):
    symbols = string.ascii_uppercase + string.ascii_lowercase + string.digits[2:]
    symbols = ''.join([symbol for symbol in symbols if symbol not in 'IloO'])
    return ''.join(random.sample(symbols, length))
def main(n, m):
    return [generate_password(m) for _ in range(n)]

print("Случайный пароль из 7 символов:", generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")