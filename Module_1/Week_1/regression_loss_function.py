import math
import random

def calculate_metrics(type_loss, y_true, y_pred):
    if type_loss == "MSE":
        return cal_mse(y_pred, y_true)
    elif type_loss == "RMSE":
        return cal_rmse(y_pred, y_true)
    elif type_loss == "MAE":
        return cal_mae(y_pred, y_true)
    else:
        raise ValueError("Invalid loss type:", type_loss)

def cal_mse(y_pred, y_true):
    return (y_true - y_pred)**2

def cal_rmse(y_pred, y_true):
    mse = cal_mse(y_pred, y_true)
    return math.sqrt(mse)

def cal_mae(y_pred, y_true):
    return abs(y_true - y_pred)
    
def regression_loss():
    x = input("Input number of samples ( integer number ) which are generated : ")
    def is_number ( n ) :
        try :
        float ( n ) # Type - casting the string to ‘float ‘.
        # If string is not a valid ‘float ‘ ,
        # it ’ll raise ‘ValueError ‘ exception
        except ValueError :
            return False
        return True

    if is_number(x) == False:
        print("Number of samples must be an integer number")
        raise ValueError
    x = int(x)
    type_loss = input("Input loss name : ")

    # Calculation:

    for i in range(x):
        y_pred = random.uniform(0, 10)
        y_true = random.uniform(0, 10)

        loss = calculate_metrics(type_loss, y_true, y_pred)
        print(f"loss name: {type_loss}, sample: {i}, pred: {y_pred}, target: {y_true}, loss: {loss}")


