def from_string_to_list(string, container):
    numbers = string.split()
    for number in numbers:
        container.append(int(number))
    return container


a = [1, 2, 3]
from_string_to_list("1 3 99 52", a)
print(*a)