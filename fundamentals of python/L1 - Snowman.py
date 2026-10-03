import turtle
t = turtle.Turtle()
t.speed(10)

sc = turtle.Screen()
sc.bgcolor('navy')

#base circle
t.pencolor('black')
t.fillcolor('yellow')

t.begin_fill()
for i in range(36):
  t.forward(13)
  t.right(10)
t.end_fill()

t.begin_fill()
for i in range(36):
  t.forward(9)
  t.left(10)
t.end_fill()

t.penup()
t.goto(0,100)
t.pendown()
t.begin_fill()
for i in range(36):
  t.forward(6)
  t.left(10)
t.end_fill()

t.penup()
t.goto(-15,140)
t.pendown()
t.circle(4)
t.penup()
t.goto(15,140)
t.pendown()
t.circle(4)
t.penup()
t.goto(-10,120)
t.pendown()
t.right(90)
for i in range(19):
  t.forward(2)
  t.left(10)

t.hideturtle()
sc.mainloop()