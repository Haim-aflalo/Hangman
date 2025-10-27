from hangman.game import init_state, validate_guess
from hangman.words import choose_secret_words
from data import lst_words
lst = lst_words.words

if __name__ == "__main__":
    secret = choose_secret_words(lst)
    a = init_state(secret)
    g = a["guessed"]
    print(a)
    print(validate_guess("a",g))