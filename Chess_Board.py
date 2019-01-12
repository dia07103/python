import turtle

def blockcolor(color_selection):    #blockcolor is the name of the function
    if color_selection == 0:        #this function changes the color
        color_selection =1
    else:
        color_selection=0
    return color_selection

t=turtle.Pen()
t.speed(9)
y=300
color=['white','black']
color_index=0       #the color will start with white
coin_colors=['red,black']

for x in range (8): #full grid
    t.penup()
    t.setpos(-300,y)       #this is the starting position of each row
    t.pendown()
    for x in range(8): #full row
        t.begin_fill()
        t.fillcolor(color[color_index])
        for x in range(4): #one shape
            t.forward(75)
            t.right(90)
        color_index=blockcolor(color_index) #changes the color for the next square in the row
        t.end_fill()
        t.forward(75)
    color_index=blockcolor(color_index) #changes the color for the first square of the next row
    y=y-75      #changes the y co-ordinate


