from hangman.words import choose_secret_words


def init_state(secret , max_tries):
    lst = ["_"]*len(secret)
    game_dict = {"secret":secret,
                 "display":lst,
                 "guessed":{},
                 "wrong_guesses":0,
                 "max_tries":max_tries}
    return game_dict


def validate_guess(ch,guessed):
    return ch, ch not in guessed

def is_won(state):
    return "_" not in state["display"]

def is_lost(state):
    return state["max_tries"] >= state["wrong_guesses"]

def render_display(state: dict):
    return state["display"]

def render_summary(state: dict):
    return state["secret"],state["guessed"]



