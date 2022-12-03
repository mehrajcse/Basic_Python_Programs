'''Problem 3
Write a program to print out all Armstrong numbers between1 and 500. If sum
of cubes of each digit of the number is equal to the number itself, then the
number is called an Armstrong number. For example, 153 = ( 1 * 1 * 1 ) + ( 5 * 5 * 5 ) + ( 3 * 3 * 3 )'''
print("The Armstrong numbers between 1 and 500 are : ")
for num in range(1,501):
  temp=num
  sum=0
  while temp>0:
      digit=temp%10
      sum=sum+digit**3
      temp=temp//10
      if sum==num:
           print (num)

