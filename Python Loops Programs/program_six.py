'''Problrm 6
 Write a program to add first seven terms of the following series using a for
loop: 1/1! + 2/2! + 3/3! + .....'''

sum = 0
factorial = 1
for i in range(1,8):
    factorial= factorial*i
    sum= sum + i/factorial
print("Sum of first seven terms of series is = ",sum)
