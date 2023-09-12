import turtle
t = turtle.Turtle()

sides = int(input("enter the number of sides: "))
length = int(input("enter the length of each side: "))
angle = ((sides-2)*180)/sides
repeat = 0 

while repeat != sides + 1 :
    t.forward(length)
    t.right(angle)
    repeat = repeat + 1
