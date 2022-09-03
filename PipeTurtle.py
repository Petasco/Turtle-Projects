import turtle
from turtle import  *
import colorsys
turtle.title('Code With Petasco')
speed(100)
bgcolor('black')
pensize(2)
petasco =0.0

for i in range(300):
   #c = colorsys.hsv_to_rgb(petasco,1,1)
    c = colorsys.hls_to_rgb(petasco,1,1)
    color(c)
    petasco+=0.005
    rt(i)
    circle(50,i)
    fd(i)
    lt(7777)
turtle.done()