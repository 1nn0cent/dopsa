for _ in range(int(input())):
    n = [int(i) for i in input().split()]
    t = []
    copy_n = n.copy
    while n:
        if n[0] > n[-1]:
            t.append(n[0])
            n.pop(0)
        else:
            t.append(n[-1])
            n.pop()
    if t != sorted(copy_n, reverse=True):
        print('НЕТ')
    else:
        print(' '.join([str(i) for i in sorted(t, reverse=True)]))