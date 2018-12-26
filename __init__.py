import json
import random
import re


def find_letter(user_input, vocab, i=None):
    return [i.start() for i in re.finditer(user_input, vocab)]


def guessing(tries,vocab,blank_line):
    while tries > 0:
        user_input = input("Guess:")

        if user_input in vocab:
            if not(user_input in blank_line):
                index = find_letter(user_input=user_input,vocab=vocab)
                i = 0
                while i < len(index):
                    blank_line[index[i]] = user_input
                    i += 1

                if not('_' in blank_line):
                    return "you won!!!"
            else:
                print("YOU ALREADY TRIED THAT LETTER!")
        else:
            tries -= 1

        print(str(blank_line) + "  Number of Tries : " + str(tries))

    return "you lost"


def hangman_game(vocab):
    'Preliminary Conditions'
    print(introductory(vocab=vocab))
    tries = num_of_tries(vocab=vocab)
    blank_line = produce_blank_lines(vocab=vocab)
    print(blank_line)

    print(guessing(tries=tries,vocab=vocab,blank_line=blank_line))


def introductory(vocab):
    return "HANGMAN GAME. So...what you gotta do is guess and infer what the word might be. " \
           "WORD COUNT : " + str(len(vocab))


def num_of_tries(vocab):
    if len(vocab) < 7:
        return 8
    elif 7 <= len(vocab) < 10:
        return 10
    else:
        return 14


def produce_blank_lines(vocab):
    blank_line = []
    for i in vocab:
        if i.isalpha():
            blank_line += "_"
        elif i == " ":
            blank_line += " "
        else:
            blank_line += i + " "

    return blank_line


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
    data = json.load(open("vocabulary.json"))
    vocab = random.choice(list(data.keys())).lower()
    print(vocab)
    print(hangman_game(vocab=vocab))






'''
Summary :
I begin the hangman project and will finish by tomorrow. 

Tomorrow :
1. Finish Hangman Project (add unique features to it)
2. Learn about REGEX
2. Learn about Github 
4. Exercise for Github by pushing hangman project


python playing a song by typing a song
'''

