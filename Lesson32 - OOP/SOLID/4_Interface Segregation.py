""" #принцип разделения интерфейсов
#ни один клиент не должен зависеть от методов, которые он не использует
#если будем разделять методы на ролевые, более мелкие
#то клиенты будут зависеть только от тех, которые к ним имеют отношение


from abc import ABCMeta, abstractmethod

class CommunicationDevice():
    @abstractmethod
    def make_calls(self):
        pass
    
    @abstractmethod
    def send_sms(self):
        pass 
    
    @abstractmethod
    def browse_internet(self):
        pass
    
    
class SmarrtPhone(CommunicationDevice):
    @abstractmethod
    def make_calls(self):
        #impl
        pass
    
    @abstractmethod
    def send_sms(self):
        #impl
        pass 
    
    @abstractmethod
    def browse_internet(self):
        #impl
        pass
    
class LindLinePhone(CommunicationDevice):
    @abstractmethod
    def make_calls(self):
        #impl
        pass
    
    @abstractmethod
    def send_sms(self):
        #just pass or exception
        pass 
    
    @abstractmethod
    def browse_internet(self):
        #just pass or exception
        pass
    
#так как у домашних телефонов нет возможности выхода в интернет или смс, им не нужно наследовать эти возможности """

#поэтому лучше поделить роли, т.е. создать классы по "звонящим" "интернет" и тд устройствам.
from abc import ABCMeta, abstractmethod

class Calling:
    @abstractmethod
    def make_calls(self):
        pass
    
class Messagin:
    @abstractmethod
    def send_sms(self):
        pass
    
class Internet:
    @abstractmethod
    def browse_internet():
        pass
    
#и уже потом наделять этими ролями другие классы

class SmartPhone(Calling,Messagin,Internet):
    def make_calls(self):
        #код
        pass
    def send_sms(self):
        #код
        pass
    
    def browse_internet():
        #код
        pass
    
class LandLinePhone(Calling):
    def make_calls(self):
        #код
        pass