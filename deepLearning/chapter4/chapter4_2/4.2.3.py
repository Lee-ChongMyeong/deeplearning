
import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

print(x_train.shape) # (60000, 784)
print(t_train.shape) # (60000, 10)

# 미니 배치 학습
train_size = x_train.shape[0]
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size)
# 0~59999의 수 중 배치 사이즈(10)만큼 무작위로 뽑아 리턴

x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]

print('train_size',train_size)
print('batch_mask',batch_mask)
print('x_batch',x_batch)
print('t_batch',t_batch)

a = np.random.choice(60000,10)
print(a)