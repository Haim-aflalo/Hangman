from hangman.words import choose_secret_words


def init_state(secret , max_tries = 10):
    lst = ["_"]*len(secret)
    game_dict = {"s_word":secret,
                 "display":lst,
                 "guessed":{},
                 "wrong_guesses":None,
                 "max_tries":max_tries}
    return game_dict


def validate_guess(ch,guessed):
    return ch, ch not in guessed




