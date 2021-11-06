# 소프트맥스 함수
import numpy as np

def softmax(a):
    exp_a = np.exp(a)
    print(exp_a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

print(softmax([0.3, 2.9, 4.0]))