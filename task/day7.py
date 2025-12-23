import random

player_score = 0
computer_score = 0
choices = ["S", "O"]  
rounds = 5

for i in range(1,rounds+1):
    print(f"\nRound {i}:")
    player = input("Player 1: ").upper()
    computer = random.choice(choices)
    print(f"Computer: {computer}")

    if player == computer:
        print("Round Winner: Tie")
    elif player == "S" and computer == "O":
        print("Round Winner: Player 1")
        player_score += 1
    else:
        print("Round Winner: Computer")
        computer_score += 1

print(f"\nFinal Score: Player 1: {player_score} | Computer: {computer_score}")

if player_score > computer_score:
    print("Final Winner: Player 1")
elif computer_score > player_score:
    print("Final Winner: Computer")
else:
    print("Final Result: Tie")