import numpy as np

# 행렬의 곱
A = np.array([[1,2], [3,4]])
print(A.shape)

B = np.array([[5,6], [7,8]])
print(B.shape)

print(np.dot(A, B)) # 두 행렬의 곱

C = np.array([[1,2,3], [4,5,6]])
C.shape
print(C.shape)

D = np.array([[1,2], [3,4], [5,6]])
D.shape
print(D.shape)

print(np.dot(C, D)) # 두 행렬의 곱

E = np.array([[1,2], [3,4]])
E.shape

np.dot(C, E) ## Error


