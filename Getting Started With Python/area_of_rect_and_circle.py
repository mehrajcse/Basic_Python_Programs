
'''Problem 5
The length & breadth of a rectangle and radius of a circle are input through the
keyboard. Write a program to calculate the area & perimeter of the rectangle,
and the area & circumference of the c'''

#Program to calculate the area and perimeter of rectangle and
# circle whose lenth,breadth and radius are taken from user
length=int(input('Enter the length of rectangle : '))
breadth=int(input('Enter the breadth of rectangle : '))
area=length*breadth
perimeter=2*(length + breadth)
print("The area of rectangle is : ",area)
print("The perimeter of rectangle is : ",perimeter,"\n")
radius=float(input('Enter the radius of circle : '))


area_c=3.14*radius*radius
perimeter_c=2*3.14*radius
print("The area of circle is : ",area_c)
print("The circumference of circle is : ",perimeter_c,"\n")
