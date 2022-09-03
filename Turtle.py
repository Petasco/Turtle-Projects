import turtle
turtle.title('Code With Petasco')
colors = [ 'red', "blue", 'yellow','green','purple', 'orange']
petasco = turtle.Pen()

turtle.bgcolor("black")
petasco.speed(50)
for x in range(300):
    petasco.pencolor(colors[x%6])
    petasco.width(x//100+1)
    petasco.forward(x)
    petasco.left(59)


turtle.done()