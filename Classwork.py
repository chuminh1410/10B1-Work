from shutil import which
from tkinter import N
from tkinter.messagebox import YES
# Printing stuff...
print("Ticket price: For one adult cost for one-day is $20.00 \nTicket price: For one child (an adult might bring up to two childrens) cost for one-day is $12.00\nTicket price: For one senior cost for one-day is $16.00 \nTicket price: For one family ticket (up to two adults of seniors , and three childrens) cost for one-day is $60.00 \nTicket price: For group of six people or more (price is for one person) for one-day is $15.00 \n  ")
print("Ticket price: For one adult cost for two-day is $30.00 \nTicket price: For one child (an adult might bring up to two childrens) cost for two-day is $18.00\nTicket price: For one senior cost for two-day is $24.00 \nTicket price: For one family ticket (up to two adults of seniors , and three childrens) cost for two-day is $90.00 \nTicket price: For group of six people or more (price is for one person) for two-day is $22.50 \n  ")
print("Attraction is also available include:\nLion feeding is $2.50\nPengiun feeding is $2.00\nEvening barbeque (two-day ticket only) $5.00\n")
print("This is the day that are still available to book: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday. ")
# Setting up stuff... (making variable for each option)
adultone = 20.00
adulttwo = 30.00
childone = 12.00
childtwo = 18.00
seniorone = 16.00
seniortwo = 24.00
familyone = 60.00
familytwo = 90.00
groupone = 15.00
grouptwo = 22.50
lion = 2.50
penguin = 2.00
barbeque = 5.00
# Setting up for user to input stuff
total = ""
continue1 = True
while continue1 == True:
    a = input("Input 1 to choose adult one day\n 2 to choose adult for two-day\n 3 to choose child for one day\n 4 to choose child for two-day\n 5 to choose senior for one day\n 6 to choose senior for two-day\n 7 to choose family for one day\n 8 to choose family for two-day\n 9 to choose group for one day\n 10 to choose group for two-day")
    continue1 = False