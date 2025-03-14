def get_username():
    """Prompt the user to enter their name and return it."""
    while True:
        username = input("Please enter your name: ").strip()
        if username:
            return username
        print("Name cannot be empty. Please try again.")

def greet_user(username):
    """Print a greeting message to the user."""
    print(f"Hello, {username}!\n")

def main():
    """Main function to run the script."""
    username = get_username()
    greet_user(username)

if __name__ == "__main__":
    main()
