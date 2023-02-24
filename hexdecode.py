from pwn import *

#%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.

#flag = ['6f','63','69','70','7b','46','54','43','30','6c','5f','49','34','5f','74','35','6d','5f','6c','6c','30','6d','5f','79','5f','79','33','6e','35','38','61','30','32','35','65','33','ff','b7','00','7d','f7','f6','ba','f8','f7','f3','e4','40','3a']
flag = ['6f636970','7b465443','306c5f49','345f7435','6d5f6c6c','306d5f79','5f79336e','35386130','32356533','ffb7007d','f7f6baf8','f7f3e440','3a3fca00']
answer = b''
for f in flag:
    
    #print(bytes(f, 'utf-8'))
    res = p32(int(bytes(f, 'utf-8').decode(), 16))
    print(res)
    answer += res

print(answer)

#picoCTF{I_l05t_4ll_my_m0n3y_0a853e52}\