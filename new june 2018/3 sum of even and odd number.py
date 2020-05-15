sum1=0
sum2=0
n=int(input("Enter the number upto which you \n want to take sum : "))


for i in range(1,n+1):
    if (i%2==0):
        sum1=sum1+i
        
    if(i%2!=0):
        sum2=sum2+i

print("Sum of Even number = ",sum1)
print("Sum of Even number = ",sum2)
