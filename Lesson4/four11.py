n = int(input())
iq = [int(input()) for m in range(n)]

avg = 0

for i in range(n):
    avg = sum(iq[:i])/i if i > 0 else 0
    if i == 0:
        print(0)
    elif iq[i]>avg:
        print('>')
    elif iq[i]<avg:
        print('<')
    else:
        print('0')