n = int(input())
s = []
flag = False
for _ in range(n):
    s.append(int(input()))
z = int(input())
for i in range(len(s)):
    for k in range(len(s)):
        if s[i]*s[k] == z and i != k:
            flag = True
            break

if flag:
    print('ДА')
else:
    print('НЕТ')