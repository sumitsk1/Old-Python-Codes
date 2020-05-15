def add(x ,y):
    return x + y

def subtract(x ,y):
    return x -y

def multiply(x ,y):
    return x*y

def divide(x ,y):
    return x/y

def square_root(x ,y):
    return x**y

print("please make a choice:")
print("select 1 to add:")
print("select 2 to subtract:")
print("select 3 to multiply:")
print("select 4 to divide:")
print("select 5 to aquare_root")

choice=input("Enter 1/2/3/4/5 \n")

num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))



if choice=="1":
    print(str(num1+num2))

elif choice=="2":
    print(str(num1-num2))

elif choice=="3":
    print(str(num1*num2))

elif choice=="4":
    print(str(num1/num2))

elif choice=="5":
    print(str(num1**num2))

else:
    print(invalid)

