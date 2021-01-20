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

