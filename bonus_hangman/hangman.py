import random

hangman_data = open("hangman_data.txt")
data_list = list(hangman_data)

random.shuffle(data_list)

"""
def user_input(input):
    if type(input) == str and len(input) == 1:
        if input.isdigit():
            print("Please use only one letter, no number")
        else:
            print(input)
    else:
        print("Please type only strings and only one letter")
"""

def game(input):
    tries = 0
    for i, el in enumerate(data_list):
        if i == 0:
            find_word = "_ " * (len(el) - 1)
            print(find_word)
            if input:
                if type(input) == str and len(input) == 1:
                    if input.isdigit():
                        print("Please use only one letter, no number")
                    else:
                        if input in el:
                            indexed = el.index(input)
                            find_word = find_word[:indexed] + input + find_word[indexed + 1]
                            print(find_word)
                        else:
                            tries += 1
                else:
                    print("Please type only strings and only one letter")

game("e")