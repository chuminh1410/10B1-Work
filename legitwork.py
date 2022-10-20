# store data in arrays
from operator import truediv
from tkinter.tix import DisplayStyle


ticket_type = ["one adult","one child","one senior","family      ","group 6 & more"]
cost_one_day = [20.00,12.00,16.00,60.00,15.00]
cost_two_day = [30.00,18.00,24.00,90.00,22.50]
extra_attraction = ["lion feeding","penguin feed","barbeque"]
extra_attration_cost = [2.50,2.00,5.00]
# one day tickets
print("Ticket Types \t\t Cost one day")
for count in range(0,len(ticket_type)):
    print(ticket_type[count], "\t\t", cost_one_day[count])

print("\nExtra attraction \t Cost ")
for count in range (0,2):
    print(extra_attraction[count], "\t\t", extra_attration_cost[count])

# two day ticket
print("\nTicket Types \t\t Cost two days")
for count in range(0,len(ticket_type)):
    print(ticket_type[count], "\t\t", cost_two_day[count])

print("\nExtra attraction \t Cost ")
for count in range (0,3):
     print(extra_attraction[count], "\t\t", extra_attration_cost[count])

# while loop 
booking_number = 0 
print("\nWelcome to Wildlife Park booking system.\nYou may book a week in advance.\n")

bookingopen = input("Would you like to book? (Y/N")
while bookingopen == "Y":
    booking_number =  booking_number + 1
    numdays = int(input("Would you like to book for one day or two? Type 1 or 2"))
    while numdays != 1 and numdays != 2:
        numdays = int(input("Error: Would you like to book for one day or two? Type 1 or 2"))
    
    group = True
    while group == True:
        numchild = int(input("How many child tickets ?"))
        numsenior = int(input("How many senior tickets ?"))
        numfamily = int(input("How many family ?"))
        numadult = int(input("How many adult tickets ?"))
        if numadult >= 6:
            ans = input("You have 6 or more adults, would you like to change into group ticket instead ? (Y/N)")
            if ans == "Y":
                numadult = 0
                numgroup = int(input("How many people in groups ?"))
                group = False
            else:
                numadult = int(input("How many adult tickets ?"))
                numgroup = int(input("How many people in groups ?"))
                group = False
        else:
            numgroup = int(input("How many people in groups ?"))
            group = False

    if numdays == 1:
        daysofweek = input("Your booking day is: Monday, Tuesday, Wednesday, Thursday, Friday")
        total_cost = cost_one_day[0]*numadult+cost_one_day[1]*numchild+cost_one_day[2]*numsenior+cost_one_day[3]*numfamily+cost_one_day[4]*numgroup
    if numdays == 2:
        daysofweek = input("Choose between Monday and Tuesday, Tuesday and Wednesday, Wednesday and Thursday, Thursday and Friday, Saturday and Sunday, Sunday Monday")
        total_cost = cost_two_day[0]*numadult+cost_two_day[1]*numchild+cost_two_day[2]*numsenior+cost_two_day[3]*numfamily+cost_two_day[4]*numgroup

# print the whole thing out
    print("Your booking is for these day of this week:", daysofweek)
    print("The ticket are for",numadult,"adults",numchild,"children",numsenior,"seniors",numfamily,"families",numgroup,"groups")
    print("Your booking number is: ",booking_number)
    print("The total cost is:",total_cost)
    bookingopen = input("Would you like to book? (Y/N")