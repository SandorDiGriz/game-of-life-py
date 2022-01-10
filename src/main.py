from game import Game

def set_game():
    setting = True
    while setting:
        parameters = []
        print("You can also choose the one-step game mode, the chance of cell birth and the generation limit \
            \nType 'one-step' to change mode and other following the example: 'one-step 25 250'")
        parameters = input().split()
        if len(parameters) not in (1, 3):
            print("Something is wierd. Let's try again")
            continue
        elif len(parameters) == 1 and parameters[0] in ("one-step", "auto"):
            return parameters[0]
        
        for param in parameters:
            if param not in  ("one-step", "auto"):
                try:
                    int(param)
                except ValueError:
                    print("Something is wierd. Let's try again")
                    continue
        setting = False
    return ",".join(parameters)

def play():
    print("\nWelcome, stranger!\n" "\nPlease, define the size of the board  \
        \n'50 30' for example")
    rows, columns  = list(map(int, input().split()))
    print("Now you are playing with the standard settings in auto mode." +
        " To select the game mode and other parameters, write 'ok'. \nTo continue, write any other word")
    
    if input() == "ok":
        parameters = set_game()
    
    print(parameters)
    
    game = Game(rows, columns, parameters)
    
        
play()