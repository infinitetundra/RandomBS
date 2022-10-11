'''Various functions useful or maybe needed to solve to determine if 
    there are anagrams'''

def letter_counter(word):
    '''Returns the count of unique letters'''
    letter_count = {}
    for letter in word:
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1

    return letter_count

def dejumble(word_list,jumbled):
    '''Function to find words with matching characters'''
    anagram_list = []
    right_length_list = matched_length_wordlist(word_list,jumbled)
    check_word = letter_counter(jumbled)
    for word in right_length_list:
        tmp = letter_counter(word)
        if tmp == check_word:
            anagram_list.append(word)
    return anagram_list

def matched_length_wordlist(check_list, word_to_check):
    '''Function to produce a list of words of a specific
       length based on a provided word'''
    list_of_right_length = []
    for word in check_list:
        if len(word) == len(word_to_check):
            list_of_right_length.append(word)
    return list_of_right_length
