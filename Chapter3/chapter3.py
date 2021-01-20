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

# Exercise 3-3.1

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)
    

def print_width():
    print('+ - - - -', end=' ')

def print_height():
    print('|        ', end=' ')

def print_width_twice():
    do_twice(print_width)
    print('+')

def print_height_twice():
    do_twice(print_height)
    print('|')

def print_row():
    print_width_twice()
    do_four(print_height_twice)

def print_grid():
    do_twice(print_row)
    print_width_twice()

print_grid()




# Exercise 3-3.2

def print_width_four():
    do_four(print_width)
    print('+')

def print_height_four():
    do_four(print_height)
    print('|')

def print_row_four():
    print_width_four()
    do_four(print_height_four)

def print_grid_four_col():
    do_four(print_row_four)
    print_width_four()

print_grid_four_col()