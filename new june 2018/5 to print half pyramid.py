star=1

column=int(input("Enter the number of column  : "))


for i in range(1,(column*2)-1):
    for j in range(1,star):
        print(end=' *')


    if i<column:
        star=star+1
    else:
        star=star-1


    print("\n")
