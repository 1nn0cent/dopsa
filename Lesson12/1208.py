text = input().lower()
freq = {}
for char in text:
    if char.isalpha():
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

symb =''
max = 0
for char, num in freq.items():
    if num > max:
        max = num
        symb = char
print(symb)