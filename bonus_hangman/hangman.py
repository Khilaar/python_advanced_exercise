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

game("a")
"""

searched_word = data_list[0]
hidden_word = "_ " * (len(data_list[0]) - 1)

print(hidden_word)
print(searched_word)

def get_input():
    user_input = input()
    return user_input

def check_input(input):
    if type(input) == str:
        if input.isdigit() or len(input) != 1:
            print("Please use only one letter, no number")
        else:
            return input

def compare_input_solution(checked_input):
    global searched_word
    global hidden_word
    while "_" in hidden_word:
        if str(checked_input) in searched_word:
            indexes = [
                index for index in range(len(searched_word))
                if searched_word.startswith(checked_input, index)
            ]
            while checked_input in searched_word:
                print(searched_word)
                searched_word = searched_word.replace(checked_input, "")
                if " " in hidden_word:
                    hidden_word = list(filter(lambda a: a != " ", hidden_word))
                print(hidden_word)
                print(hidden_word)
                for i, el in enumerate(hidden_word):
                    if i in indexes:
                        hidden_word[i] = checked_input
                hidden_word = ''.join(hidden_word)
                print(hidden_word)
                get_input()

        else:
            print("Your letter is not contained in the hidden word")
            get_input()

compare_input_solution(check_input(get_input()))








print(searched_word)
print(hidden_word)


