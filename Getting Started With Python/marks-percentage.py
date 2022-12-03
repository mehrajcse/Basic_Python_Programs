'''Problem 3
If the marks obtained by a student in five different subjects are input through
the keyboard, find out the aggregate marks and percentage marks obtained
by the student. Assume that the maximum marks that can be obtained by a
student in each subject is 1'''
#Program to calculate the total marks and percentage obtained by a student in subjects

sub_1=int(input("Enter the marks obtained in first subject (Max Marks 100) : "))
sub_2=int(input("Enter the marks obtained in second subject (Max Marks 100) : "))
sub_3=int(input("Enter the marks obtained in third subject (Max Marks 100) : "))
sub_4=int(input("Enter the marks obtained in fourth subject (Max Marks 100): "))
sub_5=int(input("Enter the marks obtained in fifth subject (Max Marks 100) : "))
print("\n")

total_marks_obtained=sub_1+sub_2+sub_3+sub_4+sub_5
print('Total marks obtained by the student in five subjects  = ',total_marks_obtained)
maximum_marks=500
percentage=total_marks_obtained/maximum_marks*100
print('The overall percentage of the student in five subjects is : ',percentage ,"%")

