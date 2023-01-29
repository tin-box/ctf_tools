import string, sys
letters = string.ascii_lowercase
#message = "dspttjohuifsvcjdpoabrkttds"
message = sys.argv[1]

if len(sys.argv) < 2:
    print("Usage: python ceaser.py message")

def shift(letter_index, letters):
    return letters[letter_index]    

def decrypt(key, message):
    message = message.lower()
    result = ""
    for letter in message:
        if letter in letters: 
            letter_index = (letters.find(letter) - key) % len(letters)
            result += shift(letter_index, letters)
        else:
            result = result + letter
    return result

def main(message):
    for key in range(len(message)): 
        decrypted = decrypt(key,message)
        print("Key: ", key, "Msg: ", decrypted) 

main(message)