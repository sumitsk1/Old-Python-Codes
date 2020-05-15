


total=0
item=0
def addingReport():
    total=0
    print("Report Type include All Items ('A') or Total Only ('T')")
    choice=input("Choose Report Type ('A' or 'T'): ")
    if choice=="A":
            print("Input an integer to add to the total or 'Q' to qui")
    while True:
        
        inpu1=input("Enter an integer or 'Q':")
        if inpu1.isdigit()==True:
            total+=int(inpu1)
        elif inpu1=="Q":
            print("Total = " +str(total))
            break

  
addingReport()
