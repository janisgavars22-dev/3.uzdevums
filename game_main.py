
from .logic import check_guess, generate_secret
from .ui import ask_for_number, show_result

def play_game():
    secret = generate_secret()
    guess = ask_for_number()

    result = check_guess(secret, guess)
    show_result(result, secret)

if __name__ == "__main__":
    play_game()

# Refactored version update
