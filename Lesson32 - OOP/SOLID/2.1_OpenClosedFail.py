#Принцип открытости\закрытости
#Наиболее важный принцип гласит сущности программы(классы, модули и тд)
#должны быть открыты для расширения, но закрыты для изменения
#класс определен достаточно, чтобы выполнять те действия, которые он должен сделать
#дополнение новых функций возможно путем создания новых сущностей, которые расширяют
from enum import Enum
class Products(Enum):
    SHIRT = 1
    TSHIRT = 2
    PANT = 3
    SHOES = 4 #добавили shoes
    
    
    

class DiscountCalculator:
    def __init__(self, product_type, cost):
        self.product_type = product_type
        self.cost = cost

    def get_discounted_price(self):
        if self.product_type == Products.SHIRT:
            return self.cost - (self.cost*0.10)
        elif self.product_type == Products.TSHIRT:
            return self.cost - (self.cost*0.15)
        elif self.product_type == Products.PANT:
            return self.cost - (self.cost*0.25)
        elif self.product_type == Products.SHOES: #пришлось добавить 2 строчки кода
            return self.cost - (self.cost*0.35)   #пришлось добавить 2 строчки кода
        
#т.е. при добавлении нового продукта, нужно дополнять и функцию, т.е.
#класс не открыт для расширения       
        
dc_shirt = DiscountCalculator(Products.SHIRT, cost = 100)
print(dc_shirt.get_discounted_price())        
dc_tshirt = DiscountCalculator(Products.TSHIRT, cost = 100)
print(dc_tshirt.get_discounted_price())  
dc_pant = DiscountCalculator(Products.PANT, cost = 100)
print(dc_pant.get_discounted_price())            