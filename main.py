from hangman.game import init_state, validate_guess, apply_guess
from hangman.words import choose_secret_words
from data import lst_words
lst = lst_words.words

if __name__ == "__main__":
    secret = choose_secret_words(lst)
    a = init_state(secret,10)
    print(a)
    g = a["guessed"]
    print(apply_guess(a,"e"))