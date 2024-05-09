import random

def roll():
    min_val = 1
    max_val = 6
    roll = random.randint(min_val, max_val)

    return roll

while True:
    players = input("Enter the number of players (2-4): ")

    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Number of players must be between 2 - 4.")
    print("Invalid, try again.")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:

    for player_idx in range(players):
        print("\nPlayer", player_idx + 1, "turen has just started!\n")
        currunt_score = 0
        
        while True:
            should_roll = input("Would you like to roll (y): ").lower()
            if should_roll != "y":
                break
            
            roll_val = roll()

            if roll_val == 1:
                print("You rolled a 1! Turn done!")
                currunt_score = 0
                break
            else:
                currunt_score += roll_val
                print("You rolled a:", roll_val)

            print("Your score is:", currunt_score)
        
        player_scores[player_idx] += currunt_score
        print("Your total score is:", player_scores[player_idx])

