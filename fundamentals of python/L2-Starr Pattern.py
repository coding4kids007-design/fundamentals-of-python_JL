import turtle
t = turtle.Turtle()
t.pensize(4)
t.speed(10)

sc = turtle.Screen()

clr = input("What colour background do you want? ")
sc.bgcolor(clr)

clr2= input("What colour turtle do you want? ")
t.color(clr2)

count = 0
while count<20:
  t.forward(150)
  t.right(90)
  t.right(100)
  count = count+1

t.hideturtle()
sc.mainloop()