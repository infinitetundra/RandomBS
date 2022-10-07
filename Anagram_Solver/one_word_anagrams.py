'''Solving one word anagrams.'''

from load_dictionary import load

word_list = load('Dict_Files//2of4brif.txt')

def dejumble(x):
    '''Function to find words with matching characters'''
    anagram_list = []
    right_length_list = matched_length_wordlist(word_list, x)
    
    return anagram_list

def matched_length_wordlist(check_list, word_to_check):
    '''Function to produce a list of words of a specific
       length based on a provided word'''
    list_of_right_length = []
    for word in check_list:
        if len(word) == len(word_to_check):
            list_of_right_length.append(word)
    return list_of_right_length


jumbled_word = input('jumbled word in question?')
anagram_matches = dejumble(jumbled_word)
