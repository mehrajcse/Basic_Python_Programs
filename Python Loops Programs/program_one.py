'''Problem 1
Write a program to find the factorial value of any number entered through the
keyboard.'''

number=int(input("Enter a number to find factorial : "))
fact=1
for i in range(1,number+1):
    fact=fact*i
print("Factorial of number is : ",fact)

