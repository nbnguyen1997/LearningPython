# Exercise 3-1 
# Write a function named right_justify that takes a string named s as a parameter
# and prints the string with enough leading spaces so that the last letter of the string is
# in column 70 of the display:

s = "Nguyen"
t = "Binh"

def right_justify(string):
    repeat = 70 - len(string)
    print(' '*repeat+string)

right_justify(s)
right_justify(t)
right_justify(s)

# Exercise 3-2
def do_twice(f,string):
    f(string)
    f(string)

def print_spam():
    print('spam')

def print_twice(text):
    print(text)
    print(text)

do_twice(print_twice,s+t+s)

# Exercise 3-3

def draw():
    draw_width()
    draw_height()
    draw_height()
    draw_height()
    draw_height()
    draw_width()
    draw_height()
    draw_height()
    draw_height()
    draw_height()
    draw_width()
    
    
def draw_width():
    print('+','- '*4,'+','- '*4,'+')

def draw_height():
    print('|','  '*4,'|','  '*4,'|')

draw()