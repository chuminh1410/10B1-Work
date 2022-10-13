from pickle import APPEND
from re import X
from shutil import which
from tkinter import N
from tkinter.messagebox import YES
# Printing stuff...
print("Ticket price: For one adult cost for one-day is $20.00 \nTicket price: For one child (an adult might bring up to two childrens) cost for one-day is $12.00\nTicket price: For one senior cost for one-day is $16.00 \nTicket price: For one family ticket (up to two adults of seniors , and three childrens) cost for one-day is $60.00 \nTicket price: For group of six people or more (price is for one person) for one-day is $15.00 \n  ")
print("Ticket price: For one adult cost for two-day is $30.00 \nTicket price: For one child (an adult might bring up to two childrens) cost for two-day is $18.00\nTicket price: For one senior cost for two-day is $24.00 \nTicket price: For one family ticket (up to two adults of seniors , and three childrens) cost for two-day is $90.00 \nTicket price: For group of six people or more (price is for one person) for two-day is $22.50 \n  ")
print("Attraction is also available include:\nLion feeding is $2.50\nPengiun feeding is $2.00\nEvening barbeque (two-day ticket only) $5.00\n")
print("This is the day that are still available to book: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday. ")
# Setting up stuff... (making variable for each option)
cost = ['20.00', '30.00', '12.00', '18.00', '16.00',
        '24.00', '60.00', '90.00', '15.00', '22.00']
lion = 2.50
penguin = 2.00
barbeque = 5.00
# Setting up for user to input stuff
total = 0
continue1 = True
while continue1 == True:
    print("\nInput 1 to choose adult one day\n 2 to choose adult for two-day\n 3 to choose child for one day\n 4 to choose child for two-day\n 5 to choose senior for one day\n 6 to choose senior for two-day\n 7 to choose family for one day\n 8 to choose family for two-day\n 9 to choose group for one day\n 10 to choose group for two-day")
    a = int(input("Your option?:"))
    if a == 1:
        x = cost[0]
        x + total
    elif a == 2:
        x = cost[1]
        x + total
    elif a == 3:
        x = cost[2]
        x + total
    elif a == 4:
        x = cost[3]
        x + total
    elif a == 5:
        x = cost[4]
        x + total
    elif a == 6:
        x = cost[5]
        x + total
    elif a == 7:
        x = cost[6]
        x + total
    elif a == 8:
        x = cost[7]
        x + total
    elif a == 9:
        x = cost[8]
        x + total
    elif a == 10:
        x = cost[9]
        x + total

    ans = input("Do you want to buy more tickets?: (Y/N)")
    if ans == "N":
        continue1 = False
print(total)
