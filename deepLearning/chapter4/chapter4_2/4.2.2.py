import numpy as np

# 교차 엔트로피 오차
def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t*np.log(y + delta))

t = [0,0,1,0,0,0,0,0,0,0]
y = [0.1, 0.05,0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
a = cross_entropy_error(np.array(y), np.array(t))
print(a)


y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
b = cross_entropy_error(np.array(y), np.array(t))
print(b)