# Assignment 3 Question 1
# Done By: Natasha Heng Jeng Yee
# UOW ID Number: 6959684

from turtle import *

def draw_rectangle(x, y, width, height):
    print("Draw a rectangle at {0},{1} with width {2} and height {3}".format(x,y,width,height))
    penup()
    goto(x,y)
    pendown()
    for i in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    penup()       
    
def draw_triangle(x,y,length):
    print("Draw an equilateral triangle at {0},{1} with length {2}".format(x,y,length))
    penup()
    goto(x,y)
    pendown()
    for i in range(3):
        forward(70)
        left(120)    
    penup() 
    
def draw_circle(x,y,radius):
    print("Draw a circle at {0},{1} with radius {2}".format(x,y,radius))
    penup()
    goto(x,y)
    pendown()
    circle(radius)
    penup()
    
def main():
    setup()
    speed(0)
    
    draw_rectangle(10,10,50,100)
    draw_triangle(0,110,70)
    draw_circle(40,80,10)  
    
    draw_rectangle(-100,100,50,100)
    draw_triangle(-110,200,70)
    draw_circle(-80,170,10)  
    hideturtle()
    done()

main()




