from hangman.game import is_won, is_lost


def prompt_guess():
    choice = input("enter your letter ")
    return choice

def print_status(state):
    print(state["display"])
    print(state["guesses"])
    print(state["wrong_guesses"])



def print_result(state):
    word = state["display"]
    found = state["guesses"]
    if is_won(state):
        print("Well Done !!",word,found)
    elif is_lost(state):
        print("You Loose",word,found)
    return

