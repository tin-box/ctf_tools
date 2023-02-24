
#flag = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彤㔲挶戹㍽"
f=open("enc", "r")
flag = f.read()
x3 = ''
for i in range(len(flag)):
    x1 = (chr(ord(flag[i]) >> 8))
    x2 = (chr((ord(flag[i]))-((ord(flag[i])>>8)<<8)))
    x3 += x1 + x2
print(x3)
#''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
