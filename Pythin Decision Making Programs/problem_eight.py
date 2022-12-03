'''Problem 8
Given the length and breadth of a rectangle, write a program to find whether
the area of the rectangle is greater than its perimeter. For example, the area
of the rectangle with length = 5 and breadth = 4 is greater than its perimeter'''
LENGTH=5
BREADTH=4
area=LENGTH*BREADTH
perimeter=2*(LENGTH+BREADTH)
if area>perimeter:
    print("Area is greater than perimeter")
else :
    print("Area is less than perimeter")
