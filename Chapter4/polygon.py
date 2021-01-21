import turtle

bob = turtle.Turtle()

def polygon(t,n,len):
    degree = 360/n
    for i in range(n):
        t.fd(len)
        t.rt(degree)

polygon(bob,5,100)

turtle.mainloop()