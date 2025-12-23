
import random

player_score = 0
computer_score = 0
choices = ["R", "P", "S"]

for round in range(1, 4):
    print(f"\nRound {round}:")
    player = input("Player 1: ").upper()
    computer = random.choice(choices)
    print(f"Computer: {computer}")

    if player == computer:
        print(f"Round {round} Winner: Tie")
    elif (player == "R" and computer == "S") or \
         (player == "P" and computer == "R") or \
         (player == "S" and computer == "P"):
        print(f"Round {round} Winner: Player 1")
        player_score += 1
    else:
        print(f"Round {round} Winner: Computer")
        computer_score += 1

print(f"\nFinal Score: Player 1: {player_score} | Computer: {computer_score}")

if player_score > computer_score:
    print("Final Winner: Player 1")
elif computer_score > player_score:
    print("Final Winner: Computer")
else:
    print("Final Result: Tie")