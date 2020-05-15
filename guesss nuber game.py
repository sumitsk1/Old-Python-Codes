
while True:
    print("Guess the no. between 1 and 10")
    guess=int(input())

    if guess <5:
        print("You do not guesssed corectly")
        print("Please guess higher")
    
    elif guess >5:
        print("You do not guesssed corectly")
        print("Please guess lower")
        
    else:
        print("Good, you gess cirectly")
        break
