from abc import ABC, abstractmethod

class Pokemon(ABC):
    
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, name):
        pass

    @property
    @abstractmethod
    def type1(self):
        pass

    @type1.setter
    @abstractmethod
    def type1(self, type1):
        pass

    @property
    @abstractmethod
    def type2(self):
        pass

    @type2.setter
    @abstractmethod
    def type2(self, type2):
        pass

    @property
    @abstractmethod
    def hp(self):
        pass

    @hp.setter
    @abstractmethod
    def hp(self, hp):
        pass
    
    @abstractmethod
    def attack(self):
        pass