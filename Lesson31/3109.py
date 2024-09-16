class Profile:
    def __init__(self, profession):
        self.profession = profession

    def info(self):
        return ""  

    def describe(self):
        additional_info = self.info()
        print(f"Профессия: {self.profession}")
        print(f"Дополнительная информация: {additional_info}")

class Vacancy(Profile):
    def __init__(self, profession, salary):
        super().__init__(profession)  
        self.salary = salary

    def info(self):
        return f"Предлагаемая зарплата: {self.salary}"  

class Resume(Profile):
    def __init__(self, profession, work_experience):
        super().__init__(profession)  
        self.work_experience = work_experience

    def info(self):
        return f"Стаж работы: {self.work_experience}"  


vacancy = Vacancy(profession="Программист", salary=80000)
vacancy.describe()
print()  
resume = Resume(profession="Программист", work_experience="5 лет")
resume.describe()
