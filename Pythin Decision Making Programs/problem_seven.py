'''Problem 7
Write a program to check whether a triangle is valid or not, when the three
angles of the triangle are entered through the keyboard. A triangle is valid if
the sum of all the three angles is equal to 180 degrees'''

angle_one=int(input("Enter the value of first angle of triangle : "))
angle_two=int(input("Enter the value of second angle of triangle : "))
angle_three=int(input("Enter the value of third angle of triangle : "))
sum_of_angles =angle_one+angle_two+angle_three
VALID_TRIANGLE = 180
if sum_of_angles==VALID_TRIANGLE:
    print("The triangle is vlaid.")
else :
    print("Invlaid triangle")
