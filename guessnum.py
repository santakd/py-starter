import random

#    Too low: "Too low, try again."
#    Low: "Low, but getting warmer!"
#    Close: "Close, but still too low!" or "Close, but still too high!" depending on whether the guess is above or below the secret number.
#    High: "High, but getting warmer!"
#    Too high: "Too high, try again."

secret_number = random.randint(1, 100)
guesses = 0

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    guesses += 1

    if guess == secret_number:
        print("Congratulations, you guessed the secret number in", guesses, "guesses!")
        break
    elif guess < secret_number:
        if secret_number - guess < 5:
            print("Close, but still too low!")
        elif secret_number - guess < 15:
            print("Low, but getting warmer!")
        else:
            print("Too low, try again.")
    else:
        if guess - secret_number < 5:
            print("Close, but still too high!")
        elif guess - secret_number < 15:
            print("High, but getting warmer!")
        else:
            print("Too high, try again.")


