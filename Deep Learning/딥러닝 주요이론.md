## 머신러닝과 딥러닝 차이
머신러닝|딥러닝
:--:|:--:
feature selecetion 필요| 모델이 알아서 feature extraction
사람이 특징을 넣어줌|모델이 특징을 파악|
|처음 학습시키는데 어렵지만 성능 향상이 쉬움|학습시키는데 쉽지만 성능 향상이 어려움|
|적은 데이터로 가능|labeled 데이터가 많이 필요|
|Feature Engineering 중요|Overfitting 쉬움|

---

## Activation Functions(활성화 함수)
1. Step Function
   1. 미분한 값이 모두 0
   2. 전 layer에서 cost를 비교할수 없음
2. Sigmoid
   1. 미분한 값의 최댓값이 0.25
   2. Layer가 많아질수록 cost가 전 layer로 갈수록 너무 작아짐  (Vanishing gradient)
3. ReLU
   1. 입력 가중합이 음수이면 무시되어 dead 뉴런 생김
   2. 미분한 값이 0 or 1
   3. cost로 전 layer 조절 가능
4. Leaky ReLU
   1. ReLU의 dead뉴런을 보완
   2. 음수부분 기울기 a ( hyper parameter)
5. ELU(exponential ReLU)

---
* MLP (Multi-layer Perceptron)
* ANN(Artificial neural network)
* DNN(Deep neural network)
  * Hidden layer 2개 이상

*  뉴런의 hidden layer 너비를 늘리는것보다 depth를 늘리는것이 더 복잡해 짐
* Early stopping
  * 학습하면서 cost 그래프가 계단형태를 그림( 정체되다가 급격히 감소함 )
  * 급격히 감소 전에 stop할 수 있으므로 권장되지 않음