import random
MAX_TRIES = 6
HANGMAN_ASCII_ART = r"""Welcome to the game Hangman
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/ """

def prompt_player_for_guess():
    players_guess = input("Guess a letter\n")
    print (players_guess)

print(HANGMAN_ASCII_ART, "\n",MAX_TRIES)
prompt_player_for_guess()