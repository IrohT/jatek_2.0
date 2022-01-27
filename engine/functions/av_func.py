def tst():
    print("teszt")


def empty():
    return "empty like your moms brain hehe boi"


# ________________________feltesz egy kérdés amihez vannak opciók (lista verzió)______________
def questions(q_input):
    def help_dict(h_dict):
        for num, key in enumerate(h_dict.keys()):
            print(f"|{num+1}.{key}|".center(30))

    def help_list(h_list):
        for num, word in enumerate(h_list):
            print(f"|{num+1}.{word}|".center(30))

    if type(q_input) is list:
        help_list(q_input)
        question = input("mit csinálsz?:".center(30))
        return question

    elif type(q_input) is dict:
        help_dict(q_input)
        question = input("mit csinálsz?:".center(30))
        return q_input[question]


# ____________________vizsgál arra hogy valami benne van e valamiben____________
def is_in(q_string, thing_in):
    if q_string in thing_in:
        return True
    else:
        return False


# ________________________________________többféle akció végrehajtása______________________________
def action_doer(str_input, cmd1=empty, cmd2=empty, cmd3=empty, cmd4=empty, cmd5=empty):

    if str_input == '1':
        return cmd1()

    elif str_input == '2':
        return cmd2()

    elif str_input == '3':
        return cmd3()

    elif str_input == '4':
        return cmd4()

    elif str_input == '5':
        return cmd5()

    else:
        print("ilyen opció nincs")