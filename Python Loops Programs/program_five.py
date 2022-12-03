'''Problem 5
. Write a program to print all prime numbers from 1 to 300. (Hint: Use nested
loops, break and continue)'''


for number in range(1,301):
    if number>1:
        for i in range(2,number):
            if (number%i)==0:
                break
        else:
            print(number)
