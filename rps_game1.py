import random

# the options
options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)

print("Let's play Rock-Paper-Scissors! 🎮")

# ask for user input
player_choice = input("Choose your weapon (rock, paper, scissors): ").lower()

if player_choice == computer_choice:
    print(f"Both chose {player_choice}! It's a tie!")
elif (player_choice == "rock" and computer_choice == "scissors") or \
     (player_choice == "paper" and computer_choice == "rock") or \
     (player_choice == "scissors" and computer_choice == "paper"):
    print(f"Computer chose {computer_choice}. You win! 🎉")
else:
    print(f"Computer chose {computer_choice}. Computer wins! 😢")

# end of program