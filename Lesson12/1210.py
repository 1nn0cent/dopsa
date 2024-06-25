phrase = input()
count = 0
for i in range(len(phrase)):
    if phrase[i].isalnum():
        count += 1
print(count)
        