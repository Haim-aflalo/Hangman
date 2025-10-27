from hangman.words import choose_secret_words
from data import lst_words
lst = lst_words.words

if __name__ == "__main__":
    print(choose_secret_words(lst))