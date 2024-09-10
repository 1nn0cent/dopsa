class Person:
 
    def __init__(self, name, otch, surn, x):
        self.name = name
        self.otch = otch
        self.surn = surn
        self.x = x
 
    def get_phone(self):
        if 'private' in self.x:
            return self.x['private']
        else:
            return
 
    def get_name(self):
        return f'{self.surn} {self.name} {self.otch}'
 
    def get_work_phone(self):
        if 'work' in self.x:
            return self.x['work']
        else:
            return
 
    def get_sms_text(self):
        return f'Уважаемый {self.name} {self.otch}! Примите участие в нашем беспроигрышном конкурсе для физических лиц'
 

class Company:
 
    def __init__(self, name, tp, x, *a):
        self.name = name
        self.tp = tp
        self.x = x
        self.a = a
 
    def get_phone(self):
        if 'contact' in self.x:
            return self.x['contact']
        elif 'contact' not in self.x:
            for i in self.a:
                if i.get_work_phone():
                    return i.get_work_phone()
            else:
                return
 
    def get_name(self):
        return self.name
 
    def get_sms_text(self):
        return f'Для компании {self.name} есть супер предложение! Примите участие ' \
            f'в нашем беспроигрышном конкурсе для {self.tp}'

def send_sms(*objects):
    for e in objects:
        if e.get_phone():
            print(f'Отправлено СМС на номер {e.get_phone()} c текстом: {e.get_sms_text()}')
        else:
            print(f'Не удалось отправить сообщение абоненту: {e.get_name()}')
            
person1 = Person("Степан", "Петрович", "Джобсов", {"private": 555})
person2 = Person("Боря", "Иванович", "Гейтсов", {"private": 777, "work": 888})
person3 = Person("Семен", "Робертович", "Возняцкий", {"work": 789})
person4 = Person("Леонид", "Арсенович", "Торвальдсон", {})
company1 = Company("Яблочный комбинат", "ООО", {"contact": 111}, person1, person3)
company2 = Company("ПластОкно", "АО", {"non_contact": 222}, person2)
company3 = Company("Пингвинья ферма", "Ltd", {"non_contact": 333}, person4)
send_sms(person1, person2, person3,person4, company1, company2, company3)