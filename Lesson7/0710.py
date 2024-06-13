move = int(input())
phrase = input()
crypto = ""
alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
for char in phrase:
    if char in alphabet:
        
        crypto += chr(ord(char)+move)
    else:
        crypto += char
print(crypto)