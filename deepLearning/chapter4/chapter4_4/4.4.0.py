import numpy as np
import matplotlib.pylab as plt

# 기울기
# 변수가 하나인 수치미분과 비슷

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
        # x[idx] = temp_val
        # print(x[idx], 'x[idx]')
        
    return grad

print(numercial_gradient(function_2, np.array([3.0, 4.0])))
print(numercial_gradient(function_2, np.array([0.0, 2.0])))
print(numercial_gradient(function_2, np.array([3.0, 0.0])))