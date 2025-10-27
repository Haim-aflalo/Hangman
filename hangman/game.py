def init_state(secret , max_tries):
    lst = ["_"]*len(secret)
    game_dict = {"secret":secret,
                 "display":lst,
                 "guesses":set(),
                 "wrong_guesses":0,
                 "max_tries":max_tries}
    return game_dict

def validate_guess(ch,guesses):
    if len(ch) != 1:
        return True, "invalid input"
    elif ch in guesses:
        return True,"you already found this letter"
    else:
         return False,"good"

def apply_guess(state,ch):
    state["guesses"].add(ch)
    if ch in state["secret"]:
        for i in range(len(state["secret"])):
            if state["secret"][i] == ch:
                state["display"][i] = ch
        return True
    else:
        state["wrong_guesses"] += 1
        return False
def is_won(state):
    return state["secret"] == "".join(state["display"])

def is_lost(state):
    return state["max_tries"] <= state["wrong_guesses"]

def render_display(state: dict):
    return state["display"]

def render_summary(state: dict):
    return state["secret"],state["guesses"]

