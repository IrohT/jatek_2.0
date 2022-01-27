class Player:
    Food_inventory = {}
    Weapon_inventory = {}

    def __init__(self, hp, stgh, money, weapon, hunger, stamina):
        self.hp = hp
        self.stgh = stgh
        self.money = money
        self.weapon = weapon
        self.hunger = hunger
        self.stamina = stamina

    def stat(self):
        for st_key, st_val in self.__dict__.items():
            print(f"|{st_key} = {st_val}|".center(30))


class Food:

    All_food = {}

    def __init__(self, name,  food_up, bonus):
        self.name = name
        self.food_up = food_up
        self.bonus = bonus
        Food.All_food.update({self.name: self})


class Recipe:
    Recipes = []

    def __init__(self, name, ing1, ing2, ing3, ing4, f_up):
        self.name = name
        self.ing1 = ing1
        self.ing2 = ing2
        self.ing3 = ing3
        self.ing4 = ing4
        self.f_up = f_up
        Recipe.Recipes.append(self)


class Weapon:
    All_Weapon = []

    def __init__(self):
        pass
