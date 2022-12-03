'''Problem 9
Write a program to calculate Weekly pay of a person. Given a person’s work
hours for the week and regular hourly wage, calculate the total pay for the
week, taking into account overtime. Hours worked over 40 are overtime,
hence paid at 1.5 times the normal rate. While hours worked over 60 are paid
double the normal rate'''

work_hours=int(input("Enter the total work hours for week : "))
hourly_wages=int(input("Enter the hourly wages : "))
NORMAL_HOURS=40
normal_rate=hourly_wages
week_pay=work_hours*hourly_wages 
if work_hours <= NORMAL_HOURS :
    print("Your weekly sallary is : ",week_pay)
elif work_hours > NORMAL_HOURS and work_hours<= 60:
    overtime=work_hours-NORMAL_HOURS
    normal_salary=NORMAL_HOURS*hourly_wages
    overtime_salary=overtime*hourly_wages*1.5
    total_week_salary=normal_salary + overtime_salary
    print("Weekly Normal Salary is = ",week_pay)
    print("Weekly overtime Salary is = ",overtime_salary)
    print("Weekly Total Salary with overtime = ",total_week_salary)
elif work_hours >60:
    overtime=20
    normal_salary=NORMAL_HOURS*hourly_wages
    overtime_salary=overtime*hourly_wages*1.5
    total_week_salary=normal_salary + overtime_salary
    extra_overtime=work_hours-60
    extra_overtime_salary=extra_overtime*normal_rate*2
    
    full_weekly_salary=total_week_salary+extra_overtime_salary
    print("your weekly salary with overtime is =",full_weekly_salary)

    
