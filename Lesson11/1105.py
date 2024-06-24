words = input()
print(str('['+ ','.join('"'+(words.split(' '))[i] + '"' for i in range(len(words.split(' ')))) + ']'))
