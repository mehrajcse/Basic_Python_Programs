'''Problem 9
Program to print pattern '''

printt_num = 1
for i in range(4):
    for j in range((5 - i) - 1):
        print(end="   ")
    for j in range(i + 1):
        print(printt_num, end="     ")
        printt_num += 1
    print()
    