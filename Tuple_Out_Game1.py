import random
# Both player's start with a score of zero
score1 = 0
score2 = 0

# defining what each die can go up to (1:6)
dice_one = [1, 2, 3, 4, 5, 6]
dice_two = [1, 2, 3, 4, 5, 6]
dice_three = [1, 2, 3, 4, 5, 6]

# each die is set to a random number from 1-6
random_roll_one = random.choice(dice_one)
random_roll_two = random.choice(dice_two)
random_roll_three = random.choice(dice_three)

# opening statements to get players' names and describe the game to them
Player_one = input("Player 1 name: ")
Player_two = input("Player 2 name: ")
print(f"Hello {Player_one} and {Player_two}, welcome to my tuple dice game!")
print("You will each roll three dice. If two dice have the same value, they are 'fixed', and can't be re-rolled")
print("If all three dice have the same value, you have 'tupled out', and your turn ends with zero points.")
print("You may continue to re-roll a dice so long as it does not have the same value as the other two dice.")
print("The player with the highest combined dice value after both turns is the winner\n")
print(f"{Player_one} will go first.")    

# Player 1's turn:
ready1 = input(f"{Player_one} are you ready to play? (yes/no): ")
if ready1.lower() == "yes":
    
    # initial dice scores    
    print(f"Dice 1: {random_roll_one}. Dice 2: {random_roll_two}. Dice 3: {random_roll_three}.")

    # score for dice 1
    while True:
        # makes sure that the dice can only be re-rolled if it is different from both other dices
        if random_roll_one != random_roll_two and random_roll_one != random_roll_three:
            reroll1 = input(f"Would you like to re-roll dice 1? It currently has a score of {random_roll_one}. (yes/no):\n")

            if reroll1.lower() == "yes":
                new_roll1 = random.choice(dice_one)
                random_roll_one = new_roll1
                print(f"Dice 1 now has a score of {random_roll_one}")
            # dice is only changed if the user opts to re-roll
            elif reroll1.lower() == "no":
                print(f"Dice 1's score is finalized with a score of {random_roll_one}")
                break
            else:
                print("Please enter yes/no.")
        else:
            print(f"Dice 1's score is finalized with a score of {random_roll_one}")
            break

    # score for dice 2
    while True:
        # makes sure that the dice can only be re-rolled if it is different from both other dices
        if random_roll_two != random_roll_one and random_roll_two != random_roll_three:
            reroll2 = input("Would you like to re-roll dice 2? (yes/no):\n")
            if reroll2.lower() == "yes":
                new_roll2 = random.choice(dice_two)
                random_roll_two = new_roll2
                print(f"Dice 2 now has a score of {random_roll_two}")
            # dice is only changed if the user opts to re-roll
            elif reroll2.lower() == "no":
                print(f"Dice 2's score is finalized with a score of {random_roll_two}")
                break
            else:
                print("Please enter yes/no.")
        else:
            print(f"Dice 2's score is finalized with a score of {random_roll_two}")
            break
        
    # score for dice 3
    while True:
        # makes sure that the dice can only be re-rolled if it is different from both other dices
        if random_roll_three != random_roll_one and random_roll_three != random_roll_two:
            reroll3 = input("Would you like to re-roll dice 3? (yes/no):\n")
            if reroll3.lower() == "yes":
                new_roll3 = random.choice(dice_three)
                random_roll_three = new_roll3
                print(f"Dice 3 now has a score of {random_roll_three}")
            # dice is only changed if the user opts to re-roll
            elif reroll3.lower() == "no":
                print(f"Dice 3's score is finalized with a score of {random_roll_three}")
                break
            else:
                print("Please enter yes/no.")
        else:
            print(f"Dice 3's score is finalized with a score of {random_roll_three}")
            break

    score1 = random_roll_one + random_roll_two + random_roll_three
    print(f"{Player_one}'s score after round 1 is: {score1}")

elif ready1.lower() == "no":
    print("")
    









# if random_roll_one == random_roll_two or random_roll_one == random_roll_three:
#     print(f"This die is fixed with a score of {random_roll_one}")
# else:
#     second_roll = input(f"Do you want to roll the first die again? It currently has a score of {random_roll_one}")
#     if second_roll == "yes":
#         random_roll_one = random.choice(dice_one)
#         print(f"The first dice was re-rolled and now has a score of {random_roll_one}")
#     else:
#         print
        

# print(random_roll_one)
