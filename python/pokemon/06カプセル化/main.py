from pikachu import Pikachu

if __name__ == "__main__":
    pokemon = Pikachu("ピカチュウ", "でんき", "", 100)

    pokemon.change_name("テキセツ")
    print(pokemon.get_name())    # テキセツ

    pokemon.change_name("うんこ")   # 「不適切な名前です」と表示される
    print(pokemon.get_name())