'''Problem 2
The distance between two cities (in km.) is input through the keyboard. Write
a program to convert and print this distance in meters, feet, inches and
centimeters.'''

#Program to convert the KM distance into other measures like meters,feets,inches and centimeters
distance=int(input("Enter the distance between two cities in KM : "))
meter=distance*1000
print("The  input distance is ",distance, "KM")
print(distance,"KM" ,'=',meter,'Meters')
feet=distance*3280.84
print(distance,"KM" ,'=',feet,'Feet')
inches=distance*39370.
print(distance,"KM" ,'=',inches,'Inches')
centimeter=distance*100000
print(distance,"KM" ,'=',centimeter,'Centimeters \n')
