import numpy as np

# 평균 제곱 오차
def sum_squares_error(y, t):
    return 0.5 * np.sum((y-t)**2)

t = [0,0,1,0,0,0,0,0,0,0]
y = [0.1, 0.05,0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]

a = sum_squares_error(np.array(y), np.array(t))
print(a) # 0.09750000000000003 : 오차가 작음

y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
b = sum_squares_error(np.array(y), np.array(t))
print(b) # 0.5975 : 오차가 더큼