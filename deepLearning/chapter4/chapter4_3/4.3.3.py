# 편미분

def numercial_diff(f,x):
  h=1e-4
  return (f(x+h)-f(x-h))/(2*h)

def function_2(x):
    return x[0] ** 2 + x[1] ** 2

def function_tmp1(x0):
    return x0*x0 + 4.0**2.0

# 예제함수
def function_ex1(x0):
    return x0*x0 + 2**2

def function_ex2(x1):
    return 1**2 + x1*x1

print(numercial_diff(function_tmp1, 3.0))

print(numercial_diff(function_ex1, 1.0))
print(numercial_diff(function_ex2, 2.0))
               

