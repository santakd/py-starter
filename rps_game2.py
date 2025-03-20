import random

def get_computer_choice(options):
    # Randomly select the computer's choice from the options.
    return random.choice(options)

def get_player_choice(options):
    # Prompt the player to input their choice and validate it.
    while True:
        player_choice = input("Choose your weapon (rock, paper, scissors): ").lower()
        if player_choice in options:
            return player_choice
        print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")

def determine_winner(player_choice, computer_choice):
    # Determine the winner based on the player's and computer's choices.
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "player"
    else:
        return "computer"

def main():
    # Main function to play the Rock-Paper-Scissors game.
    # Define the possible options
    options = ["rock", "paper", "scissors"]

    print("Welcome to Rock-Paper-Scissors! 🎮")
    
    # Get choices
    computer_choice = get_computer_choice(options)
    player_choice = get_player_choice(options)

    # Determine the winner
    winner = determine_winner(player_choice, computer_choice)

    # Display the results
    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if winner == "tie":
        print("It's a tie! 🤝")
    elif winner == "player":
        print("You win! 🎉")
    else:
        print("Computer wins! 😢")

if __name__ == "__main__":
    main()

# end of program