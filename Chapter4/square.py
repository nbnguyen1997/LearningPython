import turtle

bob = turtle.Turtle()

def draw_square(bob,t):
    for i in range(4):
        bob.fd(t)
        bob.lt(90)

draw_square(bob,100)



turtle.mainloop()