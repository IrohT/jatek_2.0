from engine.functions.av_func import *
from engine.vars import *


def camping():
    c_list = camping_act
    the_player = data["player"]

# TODO: befejezni
    def cooking():
        c_player = the_player
        # the_ings = []
        recipe = questions(Recipe.Recipes)
        print(recipe)

    # _______evés_____
    def eater():
        e_player = the_player

        # ____evésen belüli evés vagyis maga az evés_________
        def eat(ee_player, ee_food):
            if ee_player.hunger - ee_food.food_up >= 0:
                ee_player.hunger -= ee_food.food_up
            else:
                ee_player.hunger = 0
            ee_player.Food_inventory.pop(ee_food.name)
            print(f"megetted: {ee_food.name}")

        food = questions(e_player.Food_inventory)

        if is_in(food.name, e_player.Food_inventory):
            eat(e_player, food)
        else:
            print(f"sry ma éhen hallsz, ilyet nehéz enni: {food.name}")

    # ____alvás_____
    def sleep():
        s_player = the_player
        print("aludtá egy kiadósat (bár csak a csicskák fáradnak el)")
        if s_player.stamina + 20 <= 100:
            s_player.stamina += 20
        else:
            s_player.stamina = 100

    # eat, sleep [inventory, cook, craft]
    action_doer(questions(q_input=c_list), cmd1=eater, cmd2=cooking, cmd3=0, cmd4=sleep, cmd5=0)
