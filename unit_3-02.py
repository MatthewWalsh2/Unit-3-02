# Created by: Matthew Walsh
# Created on: oct 2017
# Created for: ICS3U
# This program shows how to use an if statement

import ui
from numpy import random

# random number to guess
number_to_guess = random.randint(1, 10)
print(number_to_guess)

def check_answer_button(sender):
    # check the number vs what user selects
    
    # input
    number_entered = int(view['guess_textfield'].text)
    
    # process
    global number_to_guess
    if number_entered == number_to_guess:
        # output
        view['answer_label'].text = "You guessed right!"
    else:
        view['answer_label'].text = "Sorry, that is wrong. "

view = ui.load_view()
view.present('full_screen')
