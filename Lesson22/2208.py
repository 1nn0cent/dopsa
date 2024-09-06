import random
import string

def generate_password(length):
    upper_case = [i for i in string.ascii_uppercase if i not in 'IO']
    lower_case = [i for i in string.ascii_lowercase if i not in 'lo']
    digits = list(string.digits[2:])
    chars = upper_case + lower_case + digits
    
    result = [random.choice(i) for i in (upper_case, lower_case, digits)]
    remaining = [char for char in chars if char not in result]
    result += random.sample(remaining, length - 3)
    return ''.join(result)

def main(n, m):
    return [generate_password(m) for _ in range(n)]

print("Случайный пароль из 7 символов:" , generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")