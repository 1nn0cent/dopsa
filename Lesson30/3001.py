class FoodInfo(object):
 
    def __init__ (self,prot, fats, carb):
        self.prot = prot
        self.fats = fats
        self.carb = carb
 
    def get_proteins(self):
        return self.prot
    
    def get_fats(self):
        return self.fats
    
    def get_carbohydrates (self):
        return self.carb
    
    def get_kcalories(self):
        return 4 * self.prot + 9 * self.fats + 4 * self.carb
 
    def __add__ (self,value):
        return FoodInfo(self.prot + value.prot, self.fats + value.fats, self.carb + value.carb)
