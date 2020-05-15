path='p1.txt'

text=open(path,'r')

for line in text:
    print(line)

text.close()


