from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def set_state(self, state):
        pass

class TV(Device):
    def turn_on(self):
        print(f"{self.__class__.__name__} включен.")

    def turn_off(self):
        print(f"{self.__class__.__name__} выключен.")

class Light(Device):
    def turn_on(self):
        print(f"{self.__class__.__name__} включен.")

    def turn_off(self):
        print(f"{self.__class__.__name__} выключен.")

class SonyTV(TV):
    def set_state(self, state):
        print(f"{self.__class__.__name__} переключен на {state}.")

class SamsungTV(TV):
    def set_state(self, state):
        print(f"{self.__class__.__name__} переключен на {state}.")

class PhilipsLight(Light):
    def set_state(self, state):
        print(f"{self.__class__.__name__} яркость установлена на {state}.")

class IKEALight(Light):
    def set_state(self, state):
        print(f"{self.__class__.__name__} яркость установлена на {state}.")

class RemoteControl:
    def __init__(self, device: Device):
        self.device = device
    
    def turn_on(self):
        self.device.turn_on()
    
    def turn_off(self):
        self.device.turn_off()
    
    def set_state(self, state):
        self.device.set_state(state)

def main():
    sony_tv = SonyTV()
    samsung_tv = SamsungTV()
    philips_light = PhilipsLight()
    ikea_light = IKEALight()

    remote_for_sony = RemoteControl(sony_tv)
    remote_for_samsung = RemoteControl(samsung_tv)
    remote_for_philips = RemoteControl(philips_light)
    remote_for_ikea = RemoteControl(ikea_light)

    remote_for_sony.turn_on()
    remote_for_sony.set_state("HBO")
    remote_for_sony.turn_off()

    remote_for_samsung.turn_on()
    remote_for_samsung.set_state("CNN")
    remote_for_samsung.turn_off()

    remote_for_philips.turn_on()
    remote_for_philips.set_state("75%")
    remote_for_philips.turn_off()

    remote_for_ikea.turn_on()
    remote_for_ikea.set_state("50%")
    remote_for_ikea.turn_off()

if __name__ == "__main__":
    main()
