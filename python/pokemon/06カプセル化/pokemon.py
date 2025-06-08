from abc import ABC, abstractmethod

class Pokemon(ABC):

    def __init__(self, name, type1, type2, hp):
        self.__name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

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

    def change_name(self, newName):
        if newName == "うんこ":
            print("不適切な名前です")
            return
        self.__name = newName

    def get_name(self):
        return self.__name