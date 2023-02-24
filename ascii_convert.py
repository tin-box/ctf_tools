import sys

f=open(sys.argv[1], "r")
test = f.read().split("\n")

answer = ''
for t in test:
    try:
        answer += chr(int(t))
    except ValueError:
        print('not int')
print(answer)