import random

def main():
    # list of cities and their hints
    words = {
        "paris": ["Europe", "France"], 
        "cairo": ["Africa", "Egypt"],
        "tokyo": ["Asia", "Japan"], 
        "barcelona": ["Europe", "Spain"],
        "california": ["North America", "United States"],
        "lagos": ["Africa", "Nigeria"],
        "athena": ["Europe", "Greece"],
        "milano": ["Europe", "Italy"],
        "moscow": ["Europe", "Russia"],
        "stockholm": ["Europe", "Sweden"],
        "brazilia": ["South America", "Brazil"]
    }
    
    # Choose a random word
    word, hints = random.choice(list(words.items()))
    hangman(word, hints)

def hangman(word, hints):
    # List of colors used in terminal window
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    RESET = "\033[0m"   # Reset back to default color

    # Get user name and greet them.
    name = input("Enter your name: ").strip().title()
    print(YELLOW + f"\nWelcom {name}! Let's play Hangman!\nGuess the City" + RESET)

    guessed = ["_"] * len(word)     # letters placeholders
    attempts = 7                    # Attempts available
    used_letters = set()            # set of used letters
    hints_count = 2                 # Hints available
    hint_idx = 0                    # Hint index for using in the dict

    while attempts > 0 and "_" in guessed:
        print("\nWord: ", " ".join(guessed))
        print(f"Attempts: {attempts}")
        print(f"Type 'hint' for clue ({hints_count}).")
        print(f"Used Letters:", ", ".join(sorted(used_letters)))

        # Get the gussed number
        guess = input("Guess a letter: ").strip().lower()

        # Hint Handling
        if guess == "hint":
            # if there are hints available
            if hints:
                print(YELLOW + f"Hint: City in {hints[hint_idx]}" + RESET)
                hint_idx += 1
                hints_count -= 1
                attempts -= 1
            else:
                print(YELLOW + "No more hints available!" + RESET)
            continue

        # Get a valid letter
        if len(guess) != 1 or not guess.isalpha():
            print(YELLOW + "Please enter a single letter." + RESET)
            continue

        # Check if the guess in the used letters
        if guess in used_letters:
            print(YELLOW + "The letter is already used." + RESET)
            continue
        
        # Add the guessed letter to used letters set
        used_letters.add(guess)

        # Correct Guess
        if guess in word:
            print(GREEN + "Correct!" + RESET)
            for i, ch in enumerate(word):
                if ch == guess:
                    guessed[i] = guess
        # Wrong Guess
        else:
            print(RED + "Wrong Guess!" + RESET)
            attempts -= 1

    # End the Game
    if "_" not in guessed:
        win = True
        print(GREEN + f"\nCongrats {name}! You guessed the city: {word}" + RESET)
        print_hangman(win)
    else:
        win = False
        print(RED + f"\nGame Over! :(\nThe city was: {word}" + RESET)
        print_hangman(win)


# Function to print hangman using ASCII art.
def print_hangman(win):
    if win:
        print(
        """
     |
   -------------
     |       |
     |       \\O
     |       /|\\
     |       / \\
     |
        """)
    else:
        print(
        """
        \\O/
         |
        / \\
        """)


if __name__ == "__main__":
    main()