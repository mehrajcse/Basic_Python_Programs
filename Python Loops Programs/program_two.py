'''Problem 2
Two numbers are entered through the keyboard. Write a program to find the
value of one number raised to the popwer of another.'''

base=int(input("Enter the base number : "))
power=int(input("Enter the power to the base : "))
value=1
for i in range(1,power+1):
    value=value*base
print("The result of ",base," raise power  ",power," = ",value)
