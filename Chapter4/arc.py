import turtle

bob = turtle.Turtle()

def draw_arc(t,radius,angle):
    length = 2*radius*3.141592654/360
    for i in range(angle):
        t.fd(length)
        t.lt(1)


draw_arc(bob,100,90)
    

turtle.mainloop()