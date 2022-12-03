'''Problem 1
Ramesh’s basic salary is input through the keyboard. His dearness allowance
is 40% of basic salary, and house rent allowance is 20% of basic salary. Write
a program to calculate his gross salary'''

#Program to calculate the gross salary of Ramesh ehose basic salary and other allowance are given

basic_salary=int(input("Enter the basic salary of Ramesh in rupees: "))
dearness_allowance=40/100*basic_salary
print("Dearness allowance is 40 percent of basic salary i,e : " ,dearness_allowance ,"Rs")
rent_allowance = 20/100*basic_salary
print("Rent allowance is 20 percent i,e : " ,rent_allowance , "Rs")
gross_salary = basic_salary+dearness_allowance+rent_allowance
print("The gross salary of the Ramesh is : " ,gross_salary,"Rs\n")
