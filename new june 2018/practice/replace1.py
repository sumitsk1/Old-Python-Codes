def code_translate(text):
    print(text)
    
    words=list(text)
    
    dictt={'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6',
           'g':'7','h':'8','i':'9','j':'10','k':'11','l':'12',
           'm':'13','n':'14','o':'15','p':'16','q':'17','r':'18',
           's':'19','t':'20','u':'21','v':'22','w':'23','x':'24','y':'25','z':'26'}
           
           

    for letter in words:
        if letter=='a':
            letter=dictt['a']
        if letter=='b':
            letter=dictt['b']
        if letter=='c':
            letter=dictt['c']
        if letter=='d':
            letter=dictt['d']
        if letter=='e':
            letter=dictt['e']
        if letter=='f':
            letter=dictt['f']
        if letter=='g':
            letter=dictt['g']
        if letter=='h':
            letter=dictt['h']
        if letter=='i':
            letter=dictt['i']
        if letter=='j':
            letter=dictt['j']
        if letter=='k':
            letter=dictt['k']
        if letter=='l':
            letter=dictt['l']
        if letter=='m':
            letter=dictt['m']
        if letter=='n':
            letter=dictt['n']
        if letter=='o':
            letter=dictt['o']
        if letter=='p':
            letter=dictt['p']
        if letter=='q':
            letter=dictt['q']
        if letter=='r':
            letter=dictt['r']
        if letter=='s':
            letter=dictt['s']
        if letter=='t':
            letter=dictt['t']
        if letter=='u':
            letter=dictt['u']
        if letter=='v':
            letter=dictt['v']
        if letter=='w':
            letter=dictt['w']
        if letter=='x':
            letter=dictt['x']
        if letter=='y':
            letter=dictt['y']
        if letter=='z':
            letter=dictt['z']
    
        
        print(letter,end='')



text=input("Enter any text :").lower()
code_translate(text)
