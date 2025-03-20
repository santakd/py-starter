import random
import time

def animate_coin():
    # Display a spinning coin animation.
    frames = [
        "   __  ",
        "  /  \\ ",
        "  \\__/ ",
        "   __  ",
        "  /  \\ ",
        "  \\__/ ",
        "   __  ",
        "  /  \\ ",
        "  \\__/ ",
        "   _o_ ",  # Final resting frame (heads)
        "  o   o",  # Alternative final frame
    ]
    
    for frame in frames:
        time.sleep(0.1)  # Short delay between frames
        print("\r" + frame, end="", flush=True)
    print("\r", end="")  # Clear the line after animation

def coin_toss():
    # Simulate a coin toss and return the result.
    return random.choice(["Heads", "Tails"])

def main():
    # Main function to run the Coin Toss Game.
    print("\nWelcome to the Coin Toss Game! 🌟")
    
    while True:
        # Prompt for user input
        print("\nEnter 'Y' to toss the coin or 'N' to exit.")
        choice = input("Do you want to toss the coin? (Y/N): ").strip().upper()
        
        if choice == 'Y':
            # Toss the coin
            print("\nTossing the coin...")
            animate_coin()  # Show spinning animation
            result = coin_toss()
            # Print result with different emojis for Heads and Tails
            if result == "Heads":
                print(f"\rResult: {result} 🔺🔺")
                # print(f"\rResult: {result} 🔺 🪙")
            else:
                print(f"\rResult: {result} 🔻🔻")
                # print(f"\rResult: {result} 🔻 🐾")
        elif choice == 'N':
            # Exit the game
            print("\nThanks for playing! Goodbye! 👋\n")
            break
        else:
            # Handle invalid input
            print("\nInvalid input. Please enter 'Y' to toss or 'N' to exit.")

if __name__ == "__main__":
    main()

# end of program