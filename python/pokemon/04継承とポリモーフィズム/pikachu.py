from pokemon import Pokemon
class Pikachu(Pokemon):

    def attack(self):
        super().attack()
        print(f"{self.name} の10万ボルト!")