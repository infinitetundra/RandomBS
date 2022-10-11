'''Is one word an anagram for another word'''
from anagram_functions import letter_counter

first_word = input('First word to check\n')
second_word = input('First word to check\n')

fwc = letter_counter(first_word)
swc = letter_counter(second_word)

print(fwc == swc)
