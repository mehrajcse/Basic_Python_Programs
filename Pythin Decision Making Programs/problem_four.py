'''Problem 4
Any year is input through the keyboard. Write a program to determine whether
the year is a leap year or not. (Hint: Use the % (modulus) operator.'''
#Program to check year is leap or not
year=int(input('Enter any year : '))
if (((year % 4 == 0) & (year % 100 != 0)) |(year % 400 == 0)):
    print("Leaf Year")
else :
    print("Not Leaf year")
