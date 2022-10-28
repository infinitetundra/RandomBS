'''
Decrypt a path through a Union Route Cipher

Negative column numbers mean start at bottom and read up.
Positive column numbers mean start at top and read down.

Designed for whole-word transposition ciphers with variable rows & columns.
Assumes encryption began at either top or bottom of a column.
Key indicates the order to read columns and the direction to traverse.
Example below is for 4x4 matrix with key -1 2 -3 4
Note "0" is not allowed.
Arrows show encryption route; for negative key reads UP.

  1   2   3   4
 ___ ___ ___ ___
| ^ | | | ^ | | |  Message is written
|_|_|_V_|_|_|_V_|
| ^ | | | ^ | | |  Across each row
|_|_|_V_|_|_|_V_|
| ^ | | | ^ | | |  Is this manner
|_|_|_V_|_|_|_V_|
| ^ | | | ^ | | |  Last row is filled with dummy words
|_|_|_V_|_|_|_V_|

Required inputs - a text message, # of columns, # of rows, key string

Prints translated plaintext
'''



import sys

#USER INPUT BEGINS
#============================================================================
#The string to be decrypted(type or paste between triple-quotes)
ciphertext = """16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"""

#Number of columns in the transposition matrix:
COLS = 4

#Number of rows in the transposition matrix:
ROWS = 5

#Key with spaces between numbers; negative to read UP column (ex = -1 2 -3 4):
key = """-1 2 -3 4"""

#END OF USER INPUT - DO NOT EDIT BELOW LINE!
#============================================================================
def validate_col_row(c_list):
  """Check that input columns & rows are valid vs. message length."""
  factors = []
  len_cipher = len(c_list)
  for i in range(2, len_cipher):
    if len_cipher % i == 0:
      factors.append(i)
    print("\nLength of cipher = {}".format(len_cipher))
    print("Acceptable column/row values include: {}".format(factors))
    print()
    if ROWS * COLS != len_cipher:
      print("\nError - Input columns & rows not factors of length"
            "of cipher. Terminating program.", file=sys.stderr)
      sys.exit(1)

def key_to_int(x):
  """Turn key into list of integers & check validity."""
  key_int = [int(i) for i in x.split()]
  key_int_lo = min(key_int)
  key_int_hi = max(key_int)
  if len(key_int) != COLS or key_int_lo < -COLS or key_int_hi > COLS \
      or 0 in key_int:
      print("\nError - Problem with Key. Terminating.",
      file=sys.stderr)
      sys.exit(1)
  else:
    return key_int
  

def build_matrix(keys, cipherlist):
  """Turn every n items in a list into a new item in a list of lists."""
  start = 0
  stop = ROWS
  translation_matrix = [None] * COLS

  for k in keys:
    if k < 0: #read bottom-to-top of column
      col_items = cipherlist[start:stop]
    elif k > 0: #read top-to-bottom of column
      col_items = list((reversed(cipherlist[start:stop])))
    translation_matrix[abs(k) - 1] = col_items
    start += ROWS
    stop += ROWS
  return translation_matrix

def decrypt(y):
  """Loop through nested lists popping off last item to a string."""
  plaintext = ''

  for i in range(ROWS):
    for col_items in y:
      word = str(col_items.pop())
      plaintext += word + ' '
  return plaintext

def main():
    """Run program and print decrypted plaintext."""
    print("\nCiphertext = {}".format(ciphertext))
    print("Trying {} columns".format(COLS))
    print("Trying {} rows".format(ROWS))
    print("Trying key = {}". format(key))

    #split elements into words, not letters
    cipherlist = list(ciphertext.split())
    validate_col_row(cipherlist)
    key_int = key_to_int(key)
    translation_matrix = build_matrix(key_int, cipherlist)
    plaintext = decrypt(translation_matrix)

    print("Plaintext = {}".format(plaintext))

if __name__ == '__main__':
  main()