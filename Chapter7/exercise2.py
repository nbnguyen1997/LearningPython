import math

def eval_loop():
    """
    Takes a string and evaluates it using the Python interpreter
    """
    while True:
        string = input("Enter evaluates: ")
        if(string == "done" or string == "Done"):
            print(string)
            break
        else:
            print(eval(string))

if __name__ == "__main__":
    eval_loop()