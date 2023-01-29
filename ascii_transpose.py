import string, sys
letters = string.ascii_lowercase
message = [16,9,3,15,3,20,6,'{',20,8,5,14,21,13,2,5,18,19,13,1,19,15,14,'}']
offset = 1

def decrypt(message):
    result = ''
    for m in message:
        if m == '{' or m == '}':
            result += m
        else:
            result += letters[m-offset]
    return result
print(decrypt(message))