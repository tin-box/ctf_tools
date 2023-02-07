# I pulled the code from Ghidra dissassembler 
# and refactored it in python to give me the answer
# so i wouldn't have to hurt my brain doing it manually

local_2a = 0x4e
local_29 = 0x43
local_28 = 0x4c
local_27 = 0x2d
local_26 = 0x46
local_25 = 0x59
local_24 = 0x4f
local_23 = 0x46
local_22 = 0x2d
# The alphabet they provided to calculate the last for characters of the password
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-"
test = []
print(len(alpha))           # Tell me how  long their alphabet is
for a in alpha:             # Iterate through the alphabet string so we have an easy list/array to use
    test.append(a)          # Append each character into the list individually
# Print out the precursor %s string called out in their printf
print(chr(local_2a),chr(local_29),chr(local_28),chr(local_27),chr(local_26),chr(local_25),chr(local_24),chr(local_23),chr(local_22),  
      test[(4930 + 0x8c) % 10 + 0x34],          # run their algo and pull that charcter from their prescribed alphabet
      test[(4930 + -0x1450) % 9 + 0x34],
      test[(4930 * 10 + -0x78) % 8 + 0x34],
      test[(4930 + 0x23f0) % 7 + 0x34])

answer = ''
answer += chr(local_2a)
answer += chr(local_29)
answer += chr(local_28)
answer += chr(local_27)
answer += chr(local_26)
answer += chr(local_25)
answer += chr(local_24)
answer += chr(local_23)
answer += chr(local_22)
answer += test[(4930 + 0x8c) % 10 + 0x34]          # run their algo and pull that charcter from their prescribed alphabet
answer += test[(4930 + -0x1450) % 9 + 0x34]
answer += test[(4930 * 10 + -0x78) % 8 + 0x34]
answer += test[(4930 + 0x23f0) % 7 + 0x34]
print('Answer: ' + answer)