from operator import index

from hangman.words import choose_secret_words


def init_state(secret , max_tries):
    lst = ["_"]*len(secret)
    game_dict = {"secret":secret,
                 "display":lst,
                 "guessed":set(),
                 "wrong_guesses":0,
                 "max_tries":max_tries}
    return game_dict


def validate_guess(ch,guessed):
    return ch in guessed, "your letter not in the word"

def apply_guess(state,ch):
    secret_word = state["secret"]
    if ch in secret_word:
        letter_index = secret_word.index(ch)
        state["display"][letter_index] = ch
        return True
    else:
        return False

def is_won(state):
    return "_" not in state["display"]

def is_lost(state):
    return state["max_tries"] >= state["wrong_guesses"]

def render_display(state: dict):
    return state["display"]

def render_summary(state: dict):
    return state["secret"],state["guessed"]

