import random

# functions for each dice roll

# dice 1 roll
def dice_1():
    dice_1 = [1, 2, 3, 4, 5, 6]
    dice_1_roll = random.choice(dice_1)
    return(dice_1_roll)

# dice 2 roll
def dice_2():
    dice_2 = [1, 2, 3, 4, 5, 6]
    dice_2_roll = random.choice(dice_2)
    return dice_2_roll

# dice 3 roll
def dice_3():
    dice_3 = [1, 2, 3, 4, 5, 6]
    dice_3_roll = random.choice(dice_3)
    return dice_3_roll


# number of players from 1-6
def players():
    while True:
        try:
            num_players = int(input("Enter the number of players: "))
            if 6 >= num_players >= 1:
                return num_players
            else:
                print("Number of players must be between 1-6")
        # Only allows for integers
        except ValueError:
            print("Please enter in a number")


# winning score from 50-100
def max_score():
    while True:
        try:
            max = int(input("Enter the score limit to win: "))
            if 100 >= max >= 50:
                return max
            else:
                print("Max score must be between 50 and 100")
        # Only allows for integers
        except ValueError:
            print("Please enter in a number")

# main game loop
def game_loop():
    print("Welcome to the tuple dice game!")
    num_players = players()
    score_limit = max_score()
    scores = [0] * num_players
    end_game = False
    while not end_game:
        for i in range(num_players):
            score = 0
            dice1 = dice_1()
            dice2 = dice_2()
            dice3 = dice_3()
            print(f"Player {i + 1}'s turn:")
            print(f"Dice 1: {dice1}\nDice 2: {dice2}\nDice 3: {dice3}")
            
            while True:
                if dice1 == dice2 == dice3:
                    print("Sorry, you have tupled out. Your score that round is 0.")
                    score += 0
                    break
                
            while True:
                if dice1 == dice2 and dice3 != dice2:
                    print(f"Dice 1 and Dice 2 are locked with a score of {dice1}")
                    re_roll = input(f"Would you like to re-roll dice 3? It currently has a score of {dice3}. (yes/no): ")
                    if re_roll.lower() == "yes":
                        dice3 = dice_3()
                    elif re_roll.lower() == "no":
                        print(f"Dice 1: {dice1}\nDice 2: {dice2}\nDice 3: {dice3}")
                        score = dice1 + dice2 + dice3
                        print(f"Your score that round is: {score}")
                        break
                    else:
                        print("Please enter yes/no")
                else:
                    print("Sorry, you have tupled out. Your score that round is 0.")
                    score += 0
                    break
            
            while True:
                if dice1 == dice3 and dice2 != dice3:
                    print(f"Dice 1 and Dice 3 are locked with a score of {dice1}")
                    re_roll = input(f"Would you like to re-roll dice 2? It currently has a score of {dice2}. (yes/no): ")
                    if re_roll.lower() == "yes":
                        dice2 = dice_2()
                    elif re_roll.lower() == "no":
                        print(f"Dice 1: {dice1}\nDice 2: {dice2}\nDice 3: {dice3}")
                        score = dice1 + dice2 + dice3
                        print(f"Your score that round is: {score}")
                        break
                    else:
                        print("Please enter yes/no")
                else:
                    print("Sorry, you have tupled out. Your score that round is 0.")
                    score += 0
                    break
            
            while True:
                if dice2 == dice3 and dice1 != dice3:
                    print(f"Dice 2 and Dice 3 are locked with a score of {dice2}")
                    re_roll = input(f"Would you like to re-roll dice 1? It currently has a score of {dice1}. (yes/no): ")
                    if re_roll.lower() == "yes":
                        dice1 = dice_1()
                    elif re_roll.lower() == "no":
                        print(f"Dice 1: {dice1}\nDice 2: {dice2}\nDice 3: {dice3}")
                        score = dice1 + dice2 + dice3
                        print(f"Your score that round is: {score}")
                        break
                    else:
                        print("Please enter yes/no")
                else:
                    print("Sorry, you have tupled out. Your score that round is 0.")
                    score += 0
                    break
                
            while True:
                if dice1 != dice2 and dice1 != dice3 and dice2 != dice3:
                    ...
                
            
            
game_loop()
            