# Assignment 3 Question 2
# Done By: Natasha Heng Jeng Yee
# UOW ID Number: 6959684

from turtle import *

def draw_rectangle(shape_list):
    rectangle_index = 0
    # Search through shape_list to find position(s) with rectangle
    rectangle_index_position = getIndexPosition(shape_list, 'r')
    for i in range(len(rectangle_index_position)):
        rectangle_index = rectangle_index_position[i]
        x = int(shape_list[rectangle_index + 1])
        y = int(shape_list[rectangle_index + 2])
        width = int(shape_list[rectangle_index + 3])
        height = int(shape_list[rectangle_index + 4])
        # Draw rectangle
        penup()
        goto(x,y)
        pendown()
        for i in range(2):
            forward(width)
            left(90)
            forward(height)
            left(90)
        penup()       
    
def draw_triangle(shape_list):
    triangle_index = 0
    # Search through shape_list to find position(s) with triangle
    triangle_index_position = getIndexPosition(shape_list, "t")
    
    for i in range(len(triangle_index_position)):
        triangle_index = triangle_index_position[i]
        x = int(shape_list[triangle_index + 1])
        y = int(shape_list[triangle_index + 2])
        length = int(shape_list[triangle_index + 3])
        # Draw triangle    
        penup()
        goto(x,y)
        pendown()
        for i in range(3):
            forward(70)
            left(120)    
        penup() 
    
def draw_circle(shape_list):
    circle_index = 0
    # Search through shape_list to find position(s) with circle
    circle_index_position = getIndexPosition(shape_list, "c")
    
    for i in range(len(circle_index_position)):
        circle_index = circle_index_position[i]
        x = int(shape_list[circle_index + 1])
        y = int(shape_list[circle_index + 2])
        radius = int(shape_list[circle_index + 3])
        #Draw circle
        penup()
        goto(x,y)
        pendown()
        circle(radius)
        penup()

def getIndexPosition(list_shape, shape):
    indexList = []
    for i in range(len(list_shape)):
        if list_shape[i] == shape:
            indexList.append(i)
    return indexList

def main():
    setup()
    speed(0)
    
    # Get draw string from user
    drawstring = input("Enter shapes: ")

    drawstring_list = drawstring.split(",")
    print(drawstring_list)
    
    #Draw required shapes
    draw_rectangle(drawstring_list)
    draw_triangle(drawstring_list)
    draw_circle(drawstring_list)
    hideturtle()
    done()

main()