import numpy as np
x = np.array([-1.0, 1.0, 2.0])

# 활성화 함수
def step_function(x):
    if x > 0:
        return 1
    else:
        return 0

def step_function2(x):
    y = x > 0
    return y.astype(np.init)

print(x)

y = x > 0
print(y)

y = y.astype(int)
print(y)

