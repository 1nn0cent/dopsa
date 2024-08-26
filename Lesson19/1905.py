def ask_password(login, password, success, failure):
    vow = set('aeiouy')
    sogl = set('bcdfghjklmnpqrstvwxz')
    
    if list(filter(lambda x: x in sogl, login.lower())) != list(filter(lambda x: x in sogl, password.lower())) and len(list(filter(lambda x: x in vow, password.lower()))) != 3:
        failure(login, 'Everything is wrong')
        return 0, 'Everything is wrong'
    if list(filter(lambda x: x in sogl, login.lower())) != list(filter(lambda x: x in sogl, password.lower())):
        failure(login, 'Wrong consonants')
        return 0, 'Wrong consonants'
    if len(list(filter(lambda x: x in vow, password.lower()))) != 3:
        failure(login, 'Wrong number of vowels')
        return 0, 'Wrong number of vowels'
    success(login)
    return 1, login
 
 
def failure(*args):
    return
 
 
def success(*args):
    return
 
 
def main(log, pas):
    result, err = ask_password(log.lower(), pas.lower(), success, failure)
    if result:
        print(f"Привет, {log.lower()}!")
    else:
        print(f"Кто-то пытался притвориться пользователем {log.lower()}, но в пароле допустил ошибку: {err.upper()}.")
