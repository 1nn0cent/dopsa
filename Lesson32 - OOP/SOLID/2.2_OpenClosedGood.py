from enum import Enum
from abc import ABCMeta, abstractmethod

class DiscountCalculator:
        
    @abstractmethod
    def get_discounted_price(self):
        pass
    
class DiscountCalculatorShirt(DiscountCalculator):
    def __init__(self,cost):
        self.cost = cost 
        
    def get_discounted_price(self):
        return self.cost - (self.cost*0.10)
    
    
class DiscountCalculatorTShirt(DiscountCalculator):
    def __init__(self,cost):
        self.cost = cost 
        
    def get_discounted_price(self):
        return self.cost - (self.cost*0.15)    
   
    
class DiscountCalculatorPant(DiscountCalculator):
    def __init__(self,cost):
        self.cost = cost 
        
    def get_discounted_price(self):
        return self.cost - (self.cost*0.25)        
    
#т.е. при добавлении нового продукта, нам не надо будет менять класс
#нужно будет лишь добавить новый, т.е. расширить функционал - добави новый класс

class DiscountCalculatorShoes(DiscountCalculator):
    def __init__(self,cost):
        self.cost = cost 
        
    def get_discounted_price(self):
        return self.cost - (self.cost*0.35) 

#новый продукт - описание нового продукта
#легче тестировать каждый отдельный класс, удобнее мигрировать
dc_shirt = DiscountCalculatorShirt(100)
print(dc_shirt.get_discounted_price())        
dc_tshirt = DiscountCalculatorTShirt(100)
print(dc_tshirt.get_discounted_price())  
dc_pant = DiscountCalculatorPant(100)
print(dc_pant.get_discounted_price())    
dc_pant = DiscountCalculatorShoes(100)
print(dc_pant.get_discounted_price())    