import turtle

def distances(distance_selection):
    if distance_selection == 0:
        distance_selection =1
    else:
        distance_selection=0
    return distance_selection

def blockcolor(color_selection):    #blockcolor is the name of the function
    if color_selection == 0:        #this function changes the color
        color_selection =1
    elif color_selection ==1:
        color_selection =2
    else:
        color_selection=0
    return color_selection

t=turtle.Pen()
t.speed(9)
distance_list=[300,100]
distance=1
color_list=['green','white','black']
color_index=0
y=150

t.penup()
t.setpos(-150,150)
t.pendown()
t.begin_fill()
t.fillcolor('red')
for x in range (4):
    t.forward(distance_list[distance])
    t.right (90)
    distance=distances(distance)
t.end_fill()

distance =0


for x in range (3):
    t.penup()
    t.setpos(-50,y)
    t.pendown()
    t.begin_fill()
    t.fillcolor(color_list[color_index])
    for x in range (4):
        t.forward(distance_list[distance])
        t.right(90)
        distance=distances(distance)
    color_index=blockcolor(color_index)
    t.end_fill()
    y=y-100

turtle.done()

