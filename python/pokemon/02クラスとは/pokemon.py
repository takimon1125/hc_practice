class Pokemon:

    def __init__(self):
        self.name = "リザードン"
        self.type1 = "ほのお"
        self.type2 = "ひこう"
        self.hp = 100
        self.mp = 10

    def attack(self):
        print(f"{self.name} のこうげき！")