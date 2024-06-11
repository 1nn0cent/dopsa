password1 = input() 
if len(password1) < 8:
    print('Короткий!')
elif '123' in password1:
    print('Простой!')
if len(password1)>=8 and not '123' in password1:
    password2 = input() 
    if password1 != password2:
        print("Различаются.")
    else:
        print("OK")