coin = input()
count = 1
max = 0
for i in range(len(coin)):
    if coin[i] == 'о' and coin[i+1] == 'о':
        count += 1
        if count == 1 or count > max:
            max = count
print(max)