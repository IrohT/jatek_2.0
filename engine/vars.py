from engine.oop import *


data = {
    "game": True,
    "day": 1,
    "player": Player(hp=10, stgh=30, money=0, weapon="kolbász", stamina=100, hunger=0)
    }


actions = ["stat", "fight", "camping"]

camping_act = ["eat", "cook", "craft", "sleep", "inventory"]

alma = Food("alma", 23, None)
korte = Food("körte", 23, None)
