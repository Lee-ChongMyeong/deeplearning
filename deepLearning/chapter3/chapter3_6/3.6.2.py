import sys, os
sys.path.append(os.pardir) 
import numpy as np
import pickle
from dataset.mnist import load_mnist
from common.functions import sigmoid, softmax

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def softmax(a):
  c = np.max(a)
  exp_a = np.exp(a-c)           # 오버플로 대책
  sum_exp_a = np.sum(exp_a)
  y = exp_a / sum_exp_a
  return y

def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test

def init_network():
    #sample_weight.pkl파일에 저장된 학습된 가중치 매개변수를 읽는다
    #가중치와 편향 매개변수가 딕셔너리 변수로 저장되어 있다.
    with open("/Users/이총령/Desktop/deepLearning/deeplearning/deepLearning/chapter3/chapter3_6/sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)

    return network


def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y

#신경망의 정확도(분류가 얼마나 올바른가)를 평가
x, t = get_data()
network = init_network()
print('network', network)

accuracy_cnt = 0
for i in range(len(x)):
    y = predict(network, x[i]) #각 레이블의 확률을 넘파이 배열로 반환
    p = np.argmax(y) #배열에서 값이 가장 큰(확률이 가장 높은) 원소의 인덱스를 구함
    if p == t[i]:
        accuracy_cnt += 1

print("Accuracy: "+str(float(accuracy_cnt) / len(x)))