import numpy as np

#다차원 배열
A = np.array([1, 2, 3, 4])

print(A) # [1 2 3 4]

print(np.ndim(A)) # 1 , 배열의 차원수 확인

print(A.shape) # (4, ), 배열의 형상 확인 (원소개수), 튜플 반환

print(A.shape[0]) # 4

B = np.array([[1,2], [3,4], [5,6]])

print(B)

print(np.ndim(B))

print(B.shape)
