import string

letters = string.ascii_uppercase
msg = [16,9,3,15,3,20,6,'{',20,8,5,14,21,13,2,5,18,19,13,1,19,15,14,'}']

ans = []
offset = 0
for m in msg:
    if str(m).isdigit():
        ans.append(letters[m+(offset-1)])
    else:
        ans.append(m)  

final ="".join(ans)
print(final)