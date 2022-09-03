import turtle
turtle.title('Code With Petasco')
colors = [ 'red', "blue", 'yellow','green','purple', 'orange']
petasco = turtle.Pen()
#turtle.bgpic('D:\TECNO NEW\GBWhatsApp Images\GBWhatsApp Images/laptop.jpg')
turtle.bgcolor("black")
petasco.speed(50)
for x in range(300):
    petasco.pencolor(colors[x%6])
    petasco.width(x//100+1)
    petasco.forward(x)
    petasco.left(59)


'''petasco = turtle.Turtle()
petasco.speed(10)
turtle.bgcolor('black')
petasco.pencolor('gold')
#petasco.pensize(5)
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

    petasco.right(2)'''

turtle.done()