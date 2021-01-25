import math
def mysqrt(a):
    x = a / 2 + 1
    while True:
        y = ( x + a / x) / 2
        if ( y == x ):
            break
        x = y
        
    return x

def show_string(number_space, string):
    to_string = ''
    if(isinstance(string,str) ):
        to_string = string
    else:
        to_string = str(string)
    
    print(to_string,(number_space - len(to_string))*' ',end='')

def show_result(stt,mysqrt,math_sqrt,diff):
    show_string(5,stt)
    show_string(20,mysqrt)
    show_string(20,math_sqrt)
    show_string(25,diff)
    print()

def test_square_root():
    # print("a,\tmysqrt(a),\t\t\tmath.sqrt(a),\t\t\tdiff")
    show_result("a","mysqrt(a)","math_sqrt(a)","diff")
    show_result("-","---------","------------","----")
    
    for i in range(1,10):
        show_result(stt=i,mysqrt=mysqrt(i),math_sqrt=math.sqrt(i),diff=abs(mysqrt(i)-math.sqrt(i)))
        # print(i,"\t",mysqrt(i),"\t\t",math.sqrt(i),"\t\t",abs(mysqrt(i)-math.sqrt(i)))

test_square_root()