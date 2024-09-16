class User:
    def __init__(self, name):
        self.name = name

    def send_message(self, user, message):
        pass  

    def post(self, message):
        pass  

    def info(self):
        return ""  

    def describe(self):
        additional_info = self.info()
        print(f"Имя: {self.name}, {additional_info}")


class Person(User):
    def __init__(self, name, birthdate):
        super().__init__(name)
        self.birthdate = birthdate

    def info(self):
        return f"Дата рождения: {self.birthdate}"  

    def subscribe(self, user):
        pass  


class Community(User):
    def __init__(self, name, description):
        super().__init__(name)
        self.description = description

    def info(self):
        return f"Описание: {self.description}"  



if __name__ == "__main__":
    person = Person("Салкин", "01.08.2002")
    community = Community("ИБ-31", "Клуб программистов")
    person.describe()  
    community.describe()  
