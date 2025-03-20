import random
import time

def animate_coin():
    # Frames for the coin animation
    frames = [
        "   __  ",
        "  /  \ ",
        "  \\__/",
        "   __  ",
        "  /  \ ",
        "  \\__/",
        "   __  ",
        "  /  \ ",
        "  \\__/",
        "   _o_ ",  # Final resting frame (heads)
        "  o   o",  # Alternative final frame
    ]
    
    for frame in frames:
        time.sleep(0.1)  # Short delay between frames
        print("\r" + frame, end="")
 

def coin_toss():
    result = random.choice(["Heads", "Tails"])
    return result

# Main program loop

# Welcome message
print("\nWelcome to Coin Toss Game! 🌟")

while True:
    # Prompt for user input
    print("\nEnter 'Y' to toss the coin or any other key to exit.")
    
    # Get user input
    choice = input("Do you want to toss the coin? (Y/N): ").strip().upper()
    
    if choice == 'Y':
        # Proceed with tossing the coin
        print("\nTossing the coin...")
        animate_coin()  # Show spinning animation
        
        # Determine and display the result
        result = coin_toss()
        print("\rResult:", result, end="")
        
    else:
        # Exit the game if user doesn't enter 'Y'
        print("\nThanks for playing! Goodbye! 👋\n")
        break

# end of program 
