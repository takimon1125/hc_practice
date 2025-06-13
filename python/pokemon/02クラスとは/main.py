from pokemon import Pokemon

if __name__ == "__main__":
    poke = Pokemon()

    print(poke.name)
    print(poke.type1)
    poke.attack()
    print(poke.mp)