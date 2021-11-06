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


x, t = get_data()
network = init_network()

batch_size = 100 #배치 크기
accuracy_cnt = 0

#range: 0부터 len(x)까지 batch_size간격으로 증가하는 리스트 반환
for i in range(0, len(x), batch_size):
  x_batch = x[i:i+batch_size] #0~100, 100~200, ...
  y_batch = predict(network, x_batch) #각 레이블의 확률을 넘파이 배열로 반환
  p = np.argmax(y_batch, axis=1) #배열에서 값이 가장 큰(확률이 가장 높은) 원소의 인덱스를 구함
  #axis=1: 1번째 차원을 구성하는 각 원소에서 최댓값의 인덱스를 찾도록
  accuracy_cnt += np.sum(p == t[i:i+batch_size])
  
print("Accuracy: "+str(float(accuracy_cnt) / len(x)))