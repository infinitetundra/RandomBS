"""
1) Write plaintext

2)Remove space and capitalize

3)Stack and stagger letters in zigzag pattern

4)Merge the upper and lower rows

5)Split into groups of five



1.Buy more maine potatoes
2.BUYMOREMAINEPOTATOES

3.
B  Y  O  E  A  N  P  T  T  E
 \/ \/ \/ \/ \/ \/ \/ \/ \/ \
  U  M  R  M  I  E  O  A  O  S

4.BYOEANPTTEUMRMIEOAOS

5.BYOEA NPTTE UMRMI EOAOS
"""
#------------------------------------------------------------------------------
#USER INPUT:
#the string to be encrypted (paste between quotes):
plaintext = """Let us cross over the river and rest under the shade of the trees"""

#END OF USER INPUT - DO NOT EDIT BELOW THIS LINE!
#------------------------------------------------------------------------------

def main():
    """Run program to encrypt message using 2-rail rail fence cipher."""
    message = prep_plaintext(plaintext)
    rails = build_rails(message)
    encrypt(rails)

def prep_plaintext(txt):
    '''Step 1 and 2, strip out spaces and capitalise'''
    msg = "".join(txt.split())
    msg = msg.upper() #convention for ciphertext is uppercase
    print("\nplaintext = {}".format(plaintext))
    return msg

def build_rails(msg):
    '''Build strings with every other letter in a message'''
    evens = msg[::2]
    odds = msg[1::2]

    rails = evens + odds
    return rails

def encrypt(rails):
    '''Split letters in ciphertext into chunks of 5 & join to make string'''
    ciphertext = ' '.join([rails[i:i+5] for i in range(0, len(rails), 5)])
    print("ciphertext = {}".format(ciphertext))

if __name__ == '__main__':
    main()