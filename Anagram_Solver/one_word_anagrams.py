'''Solving one word anagrams.'''

from load_dictionary import load
from anagram_functions import dejumble

word_list = load('Dict_Files//2of4brif.txt')

jumbled_word = input('jumbled word in question?')
anagram_matches = dejumble(word_list,jumbled_word)

print(anagram_matches)
