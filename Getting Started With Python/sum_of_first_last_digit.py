'''Problem 9
If a four-digit number is input through the keyboard, write a program to obtain
the sum of the first and last digit of this number.'''
#Program to calculate the sum of first and last digit of a four-digit number
number=int(input("Enter any four digit number : "))
last_digit=number%10
first_digit=number//1000
add=last_digit + first_digit
print("The sum of first and last digit of the number ",number, "is : ",add)
