
high = 1000
low = 1
while low <= high :
    guess = (low+high)//2
    print(guess)
    response = input()
    if response == '>':
        low = guess+1
    if response == '<':
        high = guess -1
    if response == '=':
        break
