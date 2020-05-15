

def triangle(n):
	

	for i in range(0, n):
		for j in range(0, n):
			print(end=" ")
		n=n-1
		for j in range(0, i+1):
			print("* ", end="")
		print("\r")
n=int(input("Enter the NUmber of rows::  "))

triangle(n)
