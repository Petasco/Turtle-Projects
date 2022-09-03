import turtle
from turtle import  *
turtle.title('Code With Petasco')
petasco = turtle.Turtle()
s = turtle.Screen()
s = bgcolor('black')
petasco.pencolor('white')
petasco.speed(10)
for i in range(100):
    petasco.circle(190-1,90)
    petasco.lt(98)
    petasco.circle(190-1,90)
    petasco.lt(18)
turtle.done()