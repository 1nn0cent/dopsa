s = input().split()
stack = []
for i in s:
    if i == '*':
        a = stack.pop()
        b = stack.pop()
        stack.append(a * b)
    elif i == '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(a + b)
    elif i == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(b - a)
    else:
        stack.append(int(i))
print(stack[0])
