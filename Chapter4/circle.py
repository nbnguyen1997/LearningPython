import turtle
import square

bob = turtle.Turtle()

def circle(t,radius):
    length = 2*radius*3.141592654/360
    for i in range(360):
        t.fd(length)
        t.lt(1)

circle(bob,100)



turtle.mainloop()
