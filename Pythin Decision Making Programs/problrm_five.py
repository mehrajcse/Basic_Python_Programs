'''Problrem 5
A five-digit number is entered through the keyboard. Write a program to check
if the number is a palindrome or not'''

number=int(input("Enter any five digit number : "))
rev=0
fifth_digit=number%10
rev=rev*10+fifth_digit
trun5=number//10

fourth_digit=trun5%10
rev=rev*10+fourth_digit
trun4=number//100

third_digit=trun4%10
rev=rev*10+third_digit
trun3=number//1000

second_digit=trun3%10
rev=rev*10+second_digit
trun4=number//10000

first_digit=trun4%10
rev=rev*10+first_digit

if number==rev:
    print("Number is Palindrome")
else:
    print("Number is Not Palindrome")



