
t1=0
t2=1

number=int(input("Enter the number of terms you want to\nprint fibonacci series : "))

for i in range(1,number+1):
    if i==1:
        print(t1)
        continue
    if i==2:
        print(t2)
        continue

    nextTerm=t1+t2
    t1=t2
    t2=nextTerm


    print(nextTerm)

    
