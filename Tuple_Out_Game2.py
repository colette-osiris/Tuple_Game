import random

# This defines both the number of dice and the range of each dice
# Each dice is 6-sided, hence the range being 1-6
def dice(num_dice = 3):
    return [random.randint(1, 6) for _ in range(num_dice)] 

# This defines the number of players who will be playing the game
# The number of players allowed is 1-6, so the function will run until there is a user input of 1-6
def players():
    while True:
        try:
            num_players = int(input("Enter the number of players: "))
            if 6 >= num_players > 0:
                return num_players
            else:
                print("Number of players must be between 1-6")
        # Only allows for integers
        except ValueError:
            print("Please enter in a number")

# This defines the score that the winning player must reach in order to win
# This score must be between 50 and 100
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

# This is the main code for a player's turn
# Includes each scenario of pairings/tuples that can occur
def cont_roll():
    for i in range(num_players):
        score = 0
        print(f"Player {i + 1}'s turn:")
        roll = dice()
        print(f"Player {i + 1} rolled {roll}")
        locked_values = []
        roll = dice()   
        # If the user 'tuples out'
        if roll[0] == roll[1] == roll[2]:
            print("Sorry, you have tupled out :(\nYour score that round is 0.")
            score += 0
                    
        # Checks for pairs that are not tuples and locks those values
                    
        # If only dice 3 is unlocked
        while True:            
            if roll[0] == roll[1] and roll[2] != roll[1]:
                print(f"Dice 1 and 2 are locked with a score of {roll[0]}")
                locked_values.append(roll[0])
                re_roll = input(f"Would you like to re-roll dice 3? It currently has a score of {roll[2]}")
                if re_roll.lower() == "yes":
                    roll[2] = random.randint(1, 6)
                    print(f"Dice 3 now has a score of {roll[0]}")
                elif re_roll.lower() == "no":
                    roll[2] = locked_values
                    score += roll[0] + roll[1] + roll[2]
                    break
                else:
                    print("Please enter yes or no")
            else:
                print("Sorry, you have tupled out :(\nYour score that round is 0.")
                score += 0
                break
                            
        # If only dice 2 is unlocked                    
        while True:
            if roll[0] == roll[2] and roll[1] != roll[2]:
                print(f"Dice 1 and 3 are locked with a score of {roll[0]}")
                locked_values.append(roll[0])
                re_roll = input(f"Would you like to re-roll dice 2? It currently has a score of {roll[1]}")
                if re_roll.lower() == "yes":
                    roll[1] = random.randint(1, 6)
                    print(f"Dice 2 now has a score of {roll[0]}")
                elif re_roll.lower() == "no":
                    roll[1] = locked_values
                    score += roll[0] + roll[1] + roll[2]
                    break
                else:
                    print("Please enter yes or no")
            else:
                print("Sorry, you have tupled out :(\nYour score that round is 0.")
                score += 0
                break    
                    
        # If only dice 1 is unlocked
        while True:
            if roll[1] == roll[2] and roll[0] != roll[2]:
                print(f"Dice 2 and 3 are locked with a score of {roll[1]}")
                locked_values.append(roll[1])
                re_roll = input(f"Would you like to re-roll dice 1? It currently has a score of {roll[0]}")
                if re_roll.lower() == "yes":
                    roll[0] = random.randint(1, 6)
                    print(f"Dice 1 now has a score of {roll[0]}")
                elif re_roll.lower() == "no":
                    roll[0] = locked_values
                    score += roll[0] + roll[1] + roll[2]
                    break
                else:
                    print("Please enter yes or no")
            else:
                print("Sorry, you have tupled out :(\nYour score that round is 0.")
                score += 0
                break








# Main game function
def play_game():
    print("Welcome to the tuple dice game!")
    num_players = players()
    score_limit = max_score()
    scores = [0] * num_players
    end_game = False
    # Runs so long as the winning score has not been reached
    while not end_game:


    for i in range(num_players):
        score = 0
        print(f"Player {i + 1}'s turn:")
        roll = dice()
        print(f"Player {i + 1} rolled {roll}")
        locked_values = []
        roll = dice()   
        # If the user 'tuples out'
        if roll[0] == roll[1] == roll[2]:
            print("Sorry, you have tupled out :(\nYour score that round is 0.")
            score += 0
                    
        # Checks for pairs that are not tuples and locks those values
                    
        # If only dice 3 is unlocked
        while True:            
            if roll[0] == roll[1] and roll[2] != roll[1]:
                print(f"Dice 1 and 2 are locked with a score of {roll[0]}")
                locked_values.append(roll[0])
                re_roll = input(f"Would you like to re-roll dice 3? It currently has a score of {roll[2]}")
                if re_roll.lower() == "yes":
                    roll[2] = random.randint(1, 6)
                    print(f"Dice 3 now has a score of {roll[0]}")
                elif re_roll.lower() == "no":
                    roll[2] = locked_values
                    score += roll[0] + roll[1] + roll[2]
                    break
                else:
                    print("Please enter yes or no")
            else:
                print("Sorry, you have tupled out :(\nYour score that round is 0.")
                score += 0
                break
                            
        # If only dice 2 is unlocked                    
        while True:
            if roll[0] == roll[2] and roll[1] != roll[2]:
                print(f"Dice 1 and 3 are locked with a score of {roll[0]}")
                locked_values.append(roll[0])
                re_roll = input(f"Would you like to re-roll dice 2? It currently has a score of {roll[1]}")
                if re_roll.lower() == "yes":
                    roll[1] = random.randint(1, 6)
                    print(f"Dice 2 now has a score of {roll[0]}")
                elif re_roll.lower() == "no":
                    roll[1] = locked_values
                    score += roll[0] + roll[1] + roll[2]
                    break
                else:
                    print("Please enter yes or no")
            else:
                print("Sorry, you have tupled out :(\nYour score that round is 0.")
                score += 0
                break    
                    
        # If only dice 1 is unlocked
        while True:
            if roll[1] == roll[2] and roll[0] != roll[2]:
                print(f"Dice 2 and 3 are locked with a score of {roll[1]}")
                locked_values.append(roll[1])
                re_roll = input(f"Would you like to re-roll dice 1? It currently has a score of {roll[0]}")
                if re_roll.lower() == "yes":
                    roll[0] = random.randint(1, 6)
                    print(f"Dice 1 now has a score of {roll[0]}")
                elif re_roll.lower() == "no":
                    roll[0] = locked_values
                    score += roll[0] + roll[1] + roll[2]
                    break
                else:
                    print("Please enter yes or no")
            else:
                print("Sorry, you have tupled out :(\nYour score that round is 0.")
                score += 0
                break






























        
            
            # If none of the dice are locked
            while True:
                if not locked_values:
                    print("No dice are locked. You can choose to re-roll them all again.")
                    re_roll = input("Would you like to re-roll all the dice? (yes/no): ")
                    if re_roll.lower() == "yes":
                        roll = dice()
                    elif re_roll.lower() == "no":
                        print(f"Your final tally for that round was -\nDice 1: {roll[0]}\nDice 2: {roll[1]}\nDice 3: {roll[2]}")
                        score += roll[0] + roll[1] + roll[2]
                        break
                    else:
                        print("Please enter yes or no")
            
            print(f"Player {i + 1}'s final roll: {roll} with a score of {score}")
            scores[i] += score
            print(f"Player {i + 1}'s total score: {scores[i]}")
                
            
            end_game = True
            break
            
            
play_game()
        




# play_game()
    
    
# determining a winner

            
            
# dice, players, score, max points


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

dice_1()
dice_2()
dice_3()