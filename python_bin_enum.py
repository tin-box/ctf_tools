import sys

def main():
    password = 'tfzbwlyzljylawhzzdvyk'  # the values provided in the original python program
    print('password length: ' + str(len(password)))                # tell me the length of the password I entered so I can if I messed up

    counter = 0                         # counter to interate through the password
    answer = ''                         # instantiate answer string to collect... the answer
    while counter < len(password):      # while counter < 21
        x = ord(password[counter]) - 7  # x = 
        if x > ord('z'):                # if x > 122
            x += 26                     # x = x - 26
        answer += chr(x)                # concat character to answer
        counter += 1       
    print('The answer: ' + answer)
main()