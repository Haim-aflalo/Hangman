from hangman.game import init_state, validate_guess, apply_guess, render_display, is_lost, is_won
from hangman.io import prompt_guess, print_status, print_result
from hangman.words import choose_secret_words
from data import random_word


def play(word,max_tries = 6):
    game_word = choose_secret_words(word)
    game_dic = init_state(game_word,max_tries)
    guesses = game_dic["guesses"]
    choice = prompt_guess()
    while True:
        flag = True
        while flag:
            choice = prompt_guess()
            (flag, message) = validate_guess(choice, game_dic["guesses"])
            print(message)
        in_word = apply_guess(game_dic, choice)
        if in_word:
            print("it's in the word")
        else:
            print("sorry")
        print_status(game_dic)
        if is_won(game_dic):
            print_result(game_dic)
            break
        if is_lost(game_dic):
            print_result(game_dic)
            break




if __name__ == "__main__":
    new_word = random_word.lst_words
    play(new_word)


