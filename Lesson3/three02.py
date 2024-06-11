password1 = input() 
if len(password1) < 8:
    print('Короткий!')

if len(password1)>=8:
    password2 = input() 
    if password1 != password2:
        print("Различаются.")
    else:
        print("OK")
