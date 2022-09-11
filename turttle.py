from turtle import *
bgcolor('black')
speed(0)
hideturtle()
for i in range(120):
     circle(i)
     color('blue')
     circle(i*0.8)
     color('green')
     left(3)
     backward(3)

done()
