class Vehicle:
    def move(self):
        pass  


class WaterTransport(Vehicle):
    def float_on_water(self):
        pass  


class Sailboat(WaterTransport):
    def sail(self):
        pass  



class AirTransport(Vehicle):
    def fly(self):
        pass  

class Airplane(AirTransport):
    def take_off(self):
        pass  

    def land(self):
        pass  

class Airship(AirTransport):
    def float(self):
        pass  

class HotAirBalloon(Airship):
    def ascend(self):
        pass  

    def descend(self):
        pass  



class GroundTransport(Vehicle):
    def drive(self):
        pass  

class Train(GroundTransport):
    def start_journey(self):
        pass  

class Car(GroundTransport):
    def accelerate(self):
        pass  

class Bicycle(GroundTransport):
    def pedal(self):
        pass  



class AnimalDrawn(Vehicle):
    def pull_cart(self):
        pass  


class SpaceTransport(Vehicle):
    def launch(self):
        pass  

class SpaceShuttle(SpaceTransport):
    def dock(self):
        pass  

class SpaceProbe(SpaceTransport):
    def land_on_moon(self):
        pass  

