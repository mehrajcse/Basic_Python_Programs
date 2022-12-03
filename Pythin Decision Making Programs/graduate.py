'''Problrm 10
Write a program, graduate.py, that prompts students for their percentage. Print their grades according to the following criteria:
Percentage >=90 A
Percentage >=80 B
Percentage >=70 C
Percentage >=60 D
Percentage < 60 F '''
percentage=int(input("Enter your percentage : "))
if percentage>=90 and percentage<101:
    print("Your Grade is : A")
elif percentage>=80 and percentage<90:
    print("Your Grade is : B")
elif percentage>=70 and percentage<80:
    print("Your Grade is : C")
elif percentage>=60 and percentage<70:
    print("Your Grade is :  D")
elif percentage<60 and percentage>=0:
    print("Your Grade is : F")
else:
    print("Percentage should be between 0% and 100 %")
