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