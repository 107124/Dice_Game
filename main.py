# Dice game
import random


def roll_dice(dice_count):
    dice_assign =  []
    while dice_count > 0:
        dice_assign.append(random.randint(1, 6))
        dice_count -= 1
    return(dice_assign)


def handle_answer(roll):
    if roll.lower() == "y":
        return True
    elif roll.lower() == "n":
        return False

def players_turn():
    roll = input("Do you want to roll? y or n\n")

    risk = handle_answer(roll)
    dice_amount = 5
    score = 0
    temp_score = 0
    keep_dice = []
    roll_again = []

    while risk:
        result = roll_dice(dice_amount)

        if 1 not in result and 5 not in result:
            print("*You lost your points for this hand...")
            break

        for dice in result:
            if dice == 1:
                keep_dice.append(dice)
                dice_amount -= 1
                temp_score += 100
            elif dice == 5:
                keep_dice.append(dice)
                dice_amount -= 1
                temp_score += 50
            else:
                roll_again.append(dice)

        print(f"\tHand Score: {temp_score}\n\tTotal Score: {score}\n\n\tKeep: {keep_dice}\n\tRoll Again:{roll_again}\n")
        roll_again = []

        if dice_amount == 0:
            dice_amount = 5

        roll = input("Do you want to roll? y or n\n")
        risk = handle_answer(roll)

        if not risk:
            score += temp_score
    else:
        print(f"You earned +{temp_score} Points\nNew Score Total: {score}\nNext players turn!")


run_game = True
player_count = int(input("How many players?\n"))
counter = 0

while run_game:

    while counter + 1 <= player_count:
        print(f"Player {counter + 1}'s turn!")
        counter += 1
        players_turn()