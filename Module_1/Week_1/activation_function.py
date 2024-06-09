# activation fuction
import math
def sigmoid(x):
    e = math.e
    return 1/(1+e**(-x))

def relu(x):
    if x <= 0:
        return 0
    else:
        return x

def elu(x):
    e = math.e
    if x <= 0:
        return 0.01*(e**(x)-1)
    else:
        return x

def activation_function():
    x = input("Input x = ")
    def is_number ( n ) :
        try :
            float ( n ) # Type - casting the string to ‘float ‘.
            # If string is not a valid ‘float ‘ ,
            # it ’ll raise ‘ValueError ‘ exception
        except ValueError :
            return False
        return True

    if is_number(x) == False:
        print("x must be a number")
    else:
        x = float(x)
        type_func = input("Input activation Function ( sigmoid | relu | elu ) : ")

        if type_func == "sigmoid":
        result = sigmoid(x)
        print(f"{type_func}: f({x}) = {result}")
        elif type_func == "relu":
        result = relu(x)
        print(f"{type_func}: f({x}) = {result}")
        elif type_func == "elu":
        result = elu(x)
        print(f"{type_func}: f({x}) = {result}")
        else:
        print(f"{type_func} is not supportted")