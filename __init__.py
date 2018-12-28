import json
import random
import re


def find_letter(user_input, vocab):
    return [i.start() for i in re.finditer(user_input, vocab)]


def guessing(tries,vocab,underscores):
    while tries > 0:
        user_input = input("Guess:")

        if user_input in vocab:
            if user_input not in underscores:
                index = find_letter(user_input=user_input,vocab=vocab)
                i = 0
                # while i < len(index):
                #     blank_line[index[i]] = user_input
                #     i += 1
                for i in find_letter(user_input=user_input,vocab=word):
                    underscores[i] = user_input

                if not('_' in underscores):
                    return "you won!!!"
            else:
                print("YOU ALREADY TRIED THAT LETTER!")
        else:
            tries -= 1

        print(str(underscores) + "  Number of Tries : " + str(tries))

    return "you lost"


def hangman_game(vocab):
    print(
        "HANGMAN GAME. So...what you gotta do is guess and infer what the word might be. "
        "WORD COUNT : %d" % len(vocab)
    )
    tries = number_of_tries(vocab=vocab)
    underscores = produce_underscores(vocab=vocab)
    print(underscores)

    print(guessing(tries=tries,vocab=vocab,underscores=underscores))
    return

def number_of_tries(vocab):
    if len(vocab) < 7:
        return 8
    elif 7 <= len(vocab) < 10:
        return 10
    else:
        return 14


def produce_underscores(vocab):
    underscores = []
    for i in vocab:
        if i.isalpha():
            underscores += "_"
        elif i == " ":
            underscores += " "
        else:
            underscores += i + " "

    return underscores


    '''
        1. Access the individual indexes of find_letter()
        2. 
    '''

    '''
    While Loop until num_of_tries == 0
        User inputs a letter.
        Program checks if the letter is in the vocab
            If Yes:
                num_of_tries stays the same
                blank_line fills in the corresponding letter
            If No:
                num_of_tries -= 1
                blank_line stays in its original condition
    When While Loop ends, show if the user won the game or not (def result())
    '''

    '''
    Problems :
    1. How to get the index of all the occurence of a letter! (OK!)
    2. Code Introductory (How you play) and Result (If you won or lost) (Play again option included)
    3. 
    '''


if __name__ == '__main__':
    with open("vocabulary.json") as file:
        data = json.load(file)

    word = random.choice(list(data.keys())).lower()
    print(word)
    print(hangman_game(vocab=word))






'''
12/25 Summary :
I begin the hangman project and will finish by tomorrow. 

Tomorrow :
1. Finish Hangman Project (add unique features to it) (OK!) 
2. Learn about REGEX (Didn't have a chance, but I did get a taste of what it is)
2. Learn about Github (OK!)
4. Exercise for Github by pushing hangman project (OK!) 


python playing a song by typing a song

12/26 Summary :
I finished my hangman project, learned about git and github (https://www.youtube.com/watch?v=ol_UCWox9kc),
& pushed my project onto github!

Tomorrow:
1. Watch How the Internet Works 101 on Khan Academy (ALL) (1 hour)
2. Learn about REGEX (Regular expression) (1 hour)
'''

