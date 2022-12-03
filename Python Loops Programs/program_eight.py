'''Problem 8
Write a program to print the multiplication table of the number entered by the
user. The table should get displayed in the following form. 29 * 1 = 29
29 * 2 = 58.'''

number=int(input("Enter a number to print multiplication table : "))
for i in range(1,11):
    mul=number*i
    print(number,"x",i,"=",mul)