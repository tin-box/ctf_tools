import string, sys

letters = string.ascii_lowercase
#letter_offset = 13 
#message = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt}"
if len(sys.argv) < 3:
    print("Usage: python rot13.py offset message")

letter_offset = int(sys.argv[1])
message = sys.argv[2]


def trans(m, letter):
    transCharIndex = (letter.find(m) + letter_offset) % len(letter)
    return letter[transCharIndex]

def trans_rot():
    transform = ''
    for m in message:
        if m.isupper():
            transform += trans(m, letters.upper())
        elif m.islower():
            transform += trans(m, letters)
        else:
            transform += m
    return transform

print('Message: ', trans_rot())