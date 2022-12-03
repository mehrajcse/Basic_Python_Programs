'''Problem 1
 If cost price and selling price of an item is input through the keyboard, write a
program to determine whether the seller has made profit or incurred loss. Also
determine how much profit he made or loss he incurred.'''
#Program to calculate profit or loss
cp=int(input("Enter the Cost Price of an item : "))
sp=int(input("Enter the Selling Price of an item : "))
profit=sp-cp
loss=cp-sp
if cp<sp:
    print("You had made profit through selling this item")
    print("Profit : ",profit)
elif cp==sp:
    print("Neither profit nor loss")
else :
    print("You had made loss through selling this item")
    print("Loss : ",loss)

