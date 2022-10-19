"""While length of phrase < limit:
    Generate list of dictionary words that fit in name
    Present words to user
    Present remaining letters to user
    Present current phrase to user
    Ask user to input word or start over
    If user input can be made from remaining letters:
        Accept choice of new word or words from user
        Remove letters in choice from letters in name
        Return choice and remaining letters in name
    If choice is not a valid selection:
        Ask user for new choice or let user start over
    Add choice to phrase and show to user
    Generate new list of words and repeat process
When phrase length equals limit value:
    Display final phrase
    Ask user to start over or to exit"""
import sys
from collections import Counter
from load_dictionary import load

word_list = load('Dict_Files//2of4brif.txt')
word_list.append('a')
word_list.append('I')
word_list = sorted(word_list)

starting_name = input('What the name to anagramify?\n')

def find_anagrams(name, words):
    '''Read name and dictionary file and display all anagrams in name'''
    name_letter_map = Counter(name)
    anagrams = []
    for word in words:
        test = ''
        word_letter_map = Counter(word.lower())
        for letter in word:
            if word_letter_map[letter] <= name_letter_map[letter]:
                test += letter
        if Counter(test) == word_letter_map:
            anagrams.append(word)
    print(*anagrams, sep='\n')
    print()
    print('Remaining letters = {}'.format(name))
    print('Number of remaining letters = {}'.format(len(name)))
    print('Number of remaining (real word) anagrams = {}'.format(len(anagrams)))

def process_choice(name):
    '''Check user choice for validity, return choice and left-over letters'''
    while True:
        choice = input('\nMake a choice else Enter to start over or # to end: ')
        if choice == '':
            main()
        elif choice == '#':
            sys.exit()
        else:
            candidate = ''.join(choice.lower().split())
        left_over_list = list(name)
        for letter in candidate:
            if letter in left_over_list:
                left_over_list.remove(letter)
        if len(name) - len(left_over_list) == len(candidate):
            break
        else:
            print('Wont work! whoo!', file=sys.stderr)
    name = ''.join(left_over_list) #makes display more readable
    return choice, name

def main():
    '''Help user build anagram phrase for their name'''
    #remove spaces and convert to lower case
    name = ''.join(ini_name.lower().split())
    #remove hyphens in hyphenated names
    name = name.replace('-', '')

    limit = len(name)
    phrase = ''
    running = True

    while running:
        temp_phrase = phrase.replace(' ','')
        if len(temp_phrase) < limit:
            print("Length of anagram = {}".format(len(temp_phrase)))

            find_anagrams(name, word_list)
            print('Current anagram phrase =', end=' ')
            print(phrase, file=sys.stderr)

            choice, name = process_choice(name)
            phrase += choice + ' '

        elif len(temp_phrase) == limit:
            print('\n***Done***\n')
            print('Anagram of name =', end=" ")
            print(phrase, file=sys.stderr)
            print()
            try_again = input('\nTry Again? (Press enter else n to quit)\n ')
            if try_again.lower() == 'n':
                running = False
                sys.exit()
            else:
                main()
