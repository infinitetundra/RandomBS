'''
rail cyphers work by taking a certain number of words and filling columns vertically
in an alternating pattern of up and down.

factors need to be agreed upon or converyed to both writer and reader:
    -number of columns and rows
    -starting direction of path(up/down) ***SIDE-NOTE  curious to know if the same cipher works with right/left***
        =Is it better to say this is determined by starting point and ending point?
    -code words


'''

#COLS = 4
#ROWS = 5

#Start of position, Bottom Left
#Plaintext = 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
#Ciphertext = 16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19
#Key = -1 2 -3 4 neg numbers mean read up column vs down

#What I Expected |  Whats shown in figure/right way to do it
#============================================================
#   v    v       |      v     v
#|4|5|14|19|     |  |0 |1 |2 |3 |
#|3|6|13|18|     |  |4 |5 |6 |7 |
#|2|7|12|17|     |  |8 |9 |10|11|
#|1|8|11|16|     |  |12|13|14|15|
#|0|9|10|15|     |  |16|17|18|19|
# ^   ^          |   ^     ^


ciphertext = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"

#split elements into words, not letters

cipherlist = list(ciphertext.split())

#initializing variables
COLS = 4
ROWS = 5
key = '-1 2 -3 4' 
translation_matrix = [None] * COLS
plaintext = ''
start = 0
stop = ROWS

#Turn key_int into list of integers

key_int = [int(i) for i in key.split()]

#turn columns into items in list of lists
for k in key_int:
    if k < 0: #reading bottom-to-top of column
        col_items = cipherlist[start:stop]
    elif k > 0: # reading top-to-bottom of column
        col_items = list((reversed(cipherlist[start:stop])))
    translation_matrix[abs(k) - 1] = col_items
    start += ROWS
    stop += ROWS

print("\nciphertext = {}".format(ciphertext))
print("\ntranslation matrix =", *translation_matrix, sep="\n")
print("\nkey length = {}".format(len(key_int)))

#loop through nested list popping off last item to new list
for i in range(ROWS):
    for col_items in translation_matrix:
        word = str(col_items.pop())
        plaintext += word + ' '
print("\nplaintext = {}".format(plaintext))
