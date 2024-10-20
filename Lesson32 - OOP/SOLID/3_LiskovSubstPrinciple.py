#Принцип подстановки Барбары Лисков
#Объекты в программе могут быть заменяемы
#экземплярами их подтипов без ущерба
#корректности работы программы
#Т.е. есть тип sub,который подтип SUB,которые взаимозаменяемы

class Car():
    def __init__(self, type):
        self.type = type
        self.properties = dict()     #добавили инициализацию свойств в класс
        
    def set_properties(self, color, gear, capacity):
        self.properties['Color'] = color
        self.properties['Gear'] = gear   
        self.properties['Capacity'] = capacity   
        
    def get_properties(self):
        return self.properties
        
        
class PetrolCar(Car):
    pass

car = Car("SUV")
car.set_properties('Red', 'Auto', 6)

#car.properties = {"Color": "Red", "Gear" : "Auto", "Capacity": 6 }

petrol_car = PetrolCar("Sedan")
petrol_car.set_properties('Blue', 'Manual', 4)

#petrol_car.properties = {"Blue", "Manual", 4}

#мы не можем в Car вводить свойства как кортеж, а в petrolcar как массив
#т.е. нарушеается способ единой подстановки Лисков
#мы не можем заменить car petrolcar'ом
#лучше задавать свойства через отдельный метод

cars = [car, petrol_car]

def find_red_cars(items):
    red_cars = 0
    for item in items:
        if item.get_properties()['Color'] == 'Red':
            red_cars += 1
    print(f'Number of Red cars = {red_cars}')

find_red_cars(cars)
