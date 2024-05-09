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

print(players)
print(player_scores)

