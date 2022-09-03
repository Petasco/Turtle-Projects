import turtle
turtle.title('Code With Petasco')
petasco = turtle.Turtle()
petasco.speed(50)
turtle.bgcolor('black')
petasco.pencolor('gold')

for x in range(180):
    petasco.forward(100)
    petasco.right(30)
    petasco.forward(20)
    petasco.left(60)
    petasco.forward(50)
    petasco.right(30)

    petasco.penup()
    petasco.setposition(0,0)
    petasco.pendown()

    petasco.right(2)

turtle.done()