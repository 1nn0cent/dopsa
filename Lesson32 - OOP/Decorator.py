from abc import ABC, abstractmethod

class Coffee:
    def get_cost(self):
        return 5

    def get_description(self):
        return "Basic Coffee"

class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_description(self):
        pass

class MilkDecorator(CoffeeDecorator):
    def get_cost(self):
        return self._coffee.get_cost() + 1  

    def get_description(self):
        return self._coffee.get_description() + ", Milk"

class ChocolateDecorator(CoffeeDecorator):
    def get_cost(self):
        return self._coffee.get_cost() + 2  

    def get_description(self):
        return self._coffee.get_description() + ", Chocolate"

class CaramelDecorator(CoffeeDecorator):
    def get_cost(self):
        return self._coffee.get_cost() + 3  

    def get_description(self):
        return self._coffee.get_description() + ", Caramel"

def main():
    basic_coffee = Coffee()
    print(basic_coffee.get_description())
    print(basic_coffee.get_cost())

    milk_coffee = MilkDecorator(basic_coffee)
    print(milk_coffee.get_description())
    print(milk_coffee.get_cost())

    chocolate_milk_coffee = ChocolateDecorator(milk_coffee)
    print(chocolate_milk_coffee.get_description())
    print(chocolate_milk_coffee.get_cost())

    caramel_chocolate_milk_coffee = CaramelDecorator(chocolate_milk_coffee)
    print(caramel_chocolate_milk_coffee.get_description())
    print(caramel_chocolate_milk_coffee.get_cost())

if __name__ == "__main__":
    main()
