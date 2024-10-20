class Engine:
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return f"Engine type: {self.type}"


class Transmission:
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return f"Transmission type: {self.type}"


class Body:
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return f"Body type: {self.type}"


class Car:
    def __init__(self):
        self.engine = None
        self.transmission = None
        self.body = None

    def __str__(self):
        return f"{self.body}, {self.engine}, {self.transmission}"


class CarBuilder:
    def create_new_car(self):
        self.car = Car()

    def set_engine(self, engine_type):
        self.car.engine = Engine(engine_type)

    def set_transmission(self, transmission_type):
        self.car.transmission = Transmission(transmission_type)

    def set_body(self, body_type):
        self.car.body = Body(body_type)

    def get_car(self):
        return self.car

class CarDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_car(self):
        self.builder.create_new_car()
        self.builder.set_engine("V8")
        self.builder.set_transmission("Automatic")
        self.builder.set_body("Sedan")
        return self.builder.get_car()


class SedanBuilder(CarBuilder):
    def construct_sedan(self):
        self.create_new_car()
        self.set_engine("V6")
        self.set_transmission("Manual")
        self.set_body("Sedan")


class SUVBuilder(CarBuilder):
    def construct_suv(self):
        self.create_new_car()
        self.set_engine("V8")
        self.set_transmission("Automatic")
        self.set_body("SUV")


class SportsCarBuilder(CarBuilder):
    def construct_sports_car(self):
        self.create_new_car()
        self.set_engine("V12")
        self.set_transmission("Automatic")
        self.set_body("Sports Car")



if __name__ == "__main__":
    sedan_builder = SedanBuilder()
    director = CarDirector(sedan_builder)
    sedan = director.construct_car()
    print("Создан седан:", sedan)

    suv_builder = SUVBuilder()
    director = CarDirector(suv_builder)
    suv = director.construct_car()
    print("Создан SUV:", suv)

    sports_car_builder = SportsCarBuilder()
    director = CarDirector(sports_car_builder)
    sports_car = director.construct_car()
    print("Создан спортивный автомобиль:", sports_car)
