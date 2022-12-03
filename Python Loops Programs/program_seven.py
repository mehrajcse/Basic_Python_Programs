'''Problrm 7
Program to print a specific pattern given in question'''
for i in range(8):
    for j in range(65, 78):
        if j >= (71) + i:
            print(chr((71) - (j % 71)), end = ' ')
        
        elif j <= (71) - i:
            print(chr(j), end = ' ')
        else:
            print(end = "  ")
    print("\n", end = '')
