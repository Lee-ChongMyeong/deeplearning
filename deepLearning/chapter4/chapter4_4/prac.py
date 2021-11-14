import numpy as np
def numerical_diff(f,w):
  h=1e-4
  return (f(w+h)-f(w-h))/(2*h)

def function_tmp1(w0):
      return w0*w0+2.0**2
def function_tmp2(w1):
  return 1.0**2 +w1*w1

print("w0에 대한 편미분",numerical_diff(function_tmp1, 1.0)) # w0에 대한 편미분
print("w1에 대한 편미분",numerical_diff(function_tmp2, 2.0)) # w1에 대한 편미분