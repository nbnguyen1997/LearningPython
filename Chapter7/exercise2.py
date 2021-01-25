import math

def eval_loop():
    while True:
        string = input("Enter evaluates: ")
        if(string == "done" or string == "Done"):
            print(string)
            break
        else:
            print(eval(string))


eval_loop()