from pokemon import Pokemon
class Pikachu(Pokemon):

    def __init__(self, name, type1, type2, hp):
        self.__name = name
        self.__type1 = type1
        self.__type2 = type2
        self.__hp = hp

    @property
    def type1(self):
        return self.__type1
    
    @type1.setter
    def type1(self, type1):
        self.__type1 = type1

    @property
    def type2(self):
        return self.__type2
    
    @type2.setter
    def type2(self, type2):
        self.__type2 = type2

    @property
    def hp(self):
        return self.__hp
    
    @hp.setter
    def hp(self, hp):
        self.__hp = hp


    def attack(self):
        print(f"{super().get_name()} の10万ボルト!")