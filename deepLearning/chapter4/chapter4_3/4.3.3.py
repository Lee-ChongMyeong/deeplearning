# 편미분

def numercial_diff(f, x):
    h = 10e-50
    return (f(x + h) - f(x)) / h

def function_2(x):
    return x[0] ** 2 + x[1] ** 2

def function_tmp1(x0):
    return x0*x0 + 4.0**2.0

print(numercial_diff(function_tmp1, 3.0))
               

