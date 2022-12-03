'''Problem 7
If a five-digit number is input through the keyboard, write a program to
calculate the sum of its digits. (Hint: Use the modulus operator % '''

#Program to calculate the sum of digits of a 5-didit number
number=int(input("Enter any five digit number : "))
#variable a stores last number (5th number)
a=number%10
trun5=number//10

#variable b stores last number (4th number)
b=trun5%10
trun4=number//100

#variable c stores last number (3rd number)
c=trun4%10
trun3=number//1000

#variable d stores last number (2nd number)
d=trun3%10
trun4=number//10000

#variable e stores last number (1st number)
e=trun4%10

add=a + b + c + d + e
print("The sum of digits of the number ",number, "is : ",add)




