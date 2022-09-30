"""making some pig latin"""
vowel = ['a','e','i','o','u']

english_word = input('What do you want to make pig latin, 1 word \n')
if english_word[0][0] not in vowel:
#constants end with first letter and ay
    platin_word = (english_word[1:len(english_word)]
                + english_word[0][0] + 'ay')
    print(platin_word)
else:
#vowels end with way
    platin_word = (english_word + 'way')
    print(platin_word)
