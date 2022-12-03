'''Problrm 4
Write a program to enter the numbers till the user wants and at the end it
should display the count of positive, negative and zeros enter'''

total_numbers = int(input("How many times you want to enter the numbers?"))
pos_count=0
neg_count=0
nutral_count=0
for i in range(0,total_numbers):
    number=int(input("Enter number : "))

    if number>0:
        pos_count+=1
    elif number<0:
        neg_count+=1  
    else :
        nutral_count+=1

print("Positive numbers : ",pos_count," , Negative nos : ",neg_count," , Zeros : ",nutral_count)

print("Program Ended")
