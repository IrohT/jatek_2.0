from engine.actions.camping.camping import *

while data["game"]:
    # Player.Food_inventory.update({alma.name: alma})
    Player.Food_inventory.update({korte.name: korte})
    action_doer(questions(q_input=actions), cmd1=data["player"].stat, cmd2=tst, cmd3=camping)
