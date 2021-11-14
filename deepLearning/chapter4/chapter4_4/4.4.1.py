
import numpy as np
import matplotlib.pylab as plt

def function_2(x):
    return x[0] ** 2 + x[1] ** 2

def numercial_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x)
    
    for idx in range(x.size):
        temp_val = x[idx] 
        # print(temp_val, 'temp_val')
        
        # f(x+h) 계산
        x[idx] = temp_val + h
        fxh1 = f(x)
        
        # f(x-h) 계산
        x[idx] = temp_val - h
        fxh2 = f(x)
        
        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = temp_val
        # print(x[idx], 'x[idx]')
        
    return grad

# init_x : 초깃값, lr : learning rate, step_num : 경사법에 따른 반복횟수
def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x
    
    for i in range(step_num):
        grad = numercial_gradient(f, x)  # 기울기를 구함
        x -= lr * grad
        
    return x 

init_x = np.array([-3.0, 4.0])
print(gradient_descent(function_2, init_x = init_x, lr= 0.1, step_num = 100))

init_x = np.array([-3.0, 4.0])
print(gradient_descent(function_2, init_x = init_x, lr= 10.0, step_num = 100))

init_x = np.array([-3.0, 4.0])
print(gradient_descent(function_2, init_x = init_x, lr= 1e-10, step_num = 100))